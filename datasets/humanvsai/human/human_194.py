def p0f_impersonate(pkt, osgenre=None, osdetails=None, signature=None,
                    extrahops=0, mtu=1500, uptime=None):
    pkt = pkt.copy()
    #pkt = pkt.__class__(str(pkt))
    while pkt.haslayer(IP) and pkt.haslayer(TCP):
        pkt = pkt.getlayer(IP)
        if isinstance(pkt.payload, TCP):
            break
        pkt = pkt.payload
    
    if not isinstance(pkt, IP) or not isinstance(pkt.payload, TCP):
        raise TypeError("Not a TCP/IP packet")
    
    if uptime is None:
        uptime = random.randint(120,100*60*60*24*365)
    
    db = p0f_selectdb(pkt.payload.flags)
    if osgenre:
        pb = db.get_base()
        if pb is None:
            pb = []
        #pb = filter(lambda x: x[6] == osgenre, pb)
        pb = [ x for x in pb if x[6] == osgenre ]
        if osdetails:
            #pb = filter(lambda x: x[7] == osdetails, pb)
            pb = [ x for x in pb if x[7] == osdetails ]
    elif signature:
        pb = [signature]
    else:
        pb = p0f_getlocalsigs()[db]
    if db == p0fr_kdb:
        # 'K' quirk <=> RST+ACK
        if pkt.payload.flags & 0x4 == 0x4:
            #pb = filter(lambda x: 'K' in x[5], pb)
            pb = [ x for x in pb if 'K' in x[5] ]
        else:
            #pb = filter(lambda x: 'K' not in x[5], pb)
            pb = [ x for x in pb if 'K' not in x[5] ]
    if not pb:
        raise Kamene_Exception("No match in the p0f database")
    pers = pb[random.randint(0, len(pb) - 1)]
    
    # options (we start with options because of MSS)
    ## TODO: let the options already set if they are valid
    options = []
    if pers[4] != '.':
        for opt in pers[4].split(','):
            if opt[0] == 'M':
                # MSS might have a maximum size because of window size
                # specification
                if pers[0][0] == 'S':
                    maxmss = (2**16-1) / int(pers[0][1:])
                else:
                    maxmss = (2**16-1)
                # If we have to randomly pick up a value, we cannot use
                # kamene RandXXX() functions, because the value has to be
                # set in case we need it for the window size value. That's
                # why we use random.randint()
                if opt[1:] == '*':
                    options.append(('MSS', random.randint(1,maxmss)))
                elif opt[1] == '%':
                    coef = int(opt[2:])
                    options.append(('MSS', coef*random.randint(1,maxmss/coef)))
                else:
                    options.append(('MSS', int(opt[1:])))
            elif opt[0] == 'W':
                if opt[1:] == '*':
                    options.append(('WScale', RandByte()))
                elif opt[1] == '%':
                    coef = int(opt[2:])
                    options.append(('WScale', coef*RandNum(min=1,
                                                           max=(2**8-1)/coef)))
                else:
                    options.append(('WScale', int(opt[1:])))
            elif opt == 'T0':
                options.append(('Timestamp', (0, 0)))
            elif opt == 'T':
                if 'T' in pers[5]:
                    # FIXME: RandInt() here does not work (bug (?) in
                    # TCPOptionsField.m2i often raises "OverflowError:
                    # long int too large to convert to int" in:
                    #    oval = struct.pack(ofmt, *oval)"
                    # Actually, this is enough to often raise the error:
                    #    struct.pack('I', RandInt())
                    options.append(('Timestamp', (uptime, random.randint(1,2**32-1))))
                else:
                    options.append(('Timestamp', (uptime, 0)))
            elif opt == 'S':
                options.append(('SAckOK', ''))
            elif opt == 'N':
                options.append(('NOP', None))
            elif opt == 'E':
                options.append(('EOL', None))
            elif opt[0] == '?':
                if int(opt[1:]) in TCPOptions[0]:
                    optname = TCPOptions[0][int(opt[1:])][0]
                    optstruct = TCPOptions[0][int(opt[1:])][1]
                    options.append((optname,
                                    struct.unpack(optstruct,
                                                  RandString(struct.calcsize(optstruct))._fix())))
                else:
                    options.append((int(opt[1:]), ''))
            ## FIXME: qqP not handled
            else:
                warning("unhandled TCP option " + opt)
            pkt.payload.options = options
    
    # window size
    if pers[0] == '*':
        pkt.payload.window = RandShort()
    elif pers[0].isdigit():
        pkt.payload.window = int(pers[0])
    elif pers[0][0] == '%':
        coef = int(pers[0][1:])
        pkt.payload.window = coef * RandNum(min=1,max=(2**16-1)/coef)
    elif pers[0][0] == 'T':
        pkt.payload.window = mtu * int(pers[0][1:])
    elif pers[0][0] == 'S':
        ## needs MSS set
        #MSS = filter(lambda x: x[0] == 'MSS', options)
        MSS = [ x for x in options if x[0] == 'MSS' ]
        if not MSS:
            raise Kamene_Exception("TCP window value requires MSS, and MSS option not set")
        pkt.payload.window = MSS[0][1] * int(pers[0][1:])
    else:
        raise Kamene_Exception('Unhandled window size specification')
    
    # ttl
    pkt.ttl = pers[1]-extrahops
    # DF flag
    pkt.flags |= (2 * pers[2])
    ## FIXME: ss (packet size) not handled (how ? may be with D quirk
    ## if present)
    # Quirks
    if pers[5] != '.':
        for qq in pers[5]:
            ## FIXME: not handled: P, I, X, !
            # T handled with the Timestamp option
            if qq == 'Z': pkt.id = 0
            elif qq == 'U': pkt.payload.urgptr = RandShort()
            elif qq == 'A': pkt.payload.ack = RandInt()
            elif qq == 'F':
                #if db == p0fo_kdb:
                #    pkt.payload.flags |= 0x20 # U
                #else:
                    pkt.payload.flags |= RandChoice(8, 32, 40) #P / U / PU
            elif qq == 'D' and db != p0fo_kdb:
                pkt /= conf.raw_layer(load=RandString(random.randint(1, 10))) # XXX p0fo.fp
            elif qq == 'Q': pkt.payload.seq = pkt.payload.ack
            #elif qq == '0': pkt.payload.seq = 0
        #if db == p0fr_kdb:
        # '0' quirk is actually not only for p0fr.fp (see
        # packet2p0f())
    if '0' in pers[5]:
        pkt.payload.seq = 0
    elif pkt.payload.seq == 0:
        pkt.payload.seq = RandInt()
    
    while pkt.underlayer:
        pkt = pkt.underlayer
    return pkt