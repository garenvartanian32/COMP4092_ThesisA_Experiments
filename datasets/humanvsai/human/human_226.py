def pull(self):
        # For each packet in the pcap process the contents
        for item in self.input_stream:
            # Print out the timestamp in UTC
            print('Timestamp: %s' % item['timestamp'])
            # Unpack the Ethernet frame (mac src/dst, ethertype)
            print('Ethernet Frame: %s --> %s  (type: %d)' % \
                  (net_utils.mac_to_str(item['eth']['src']), net_utils.mac_to_str(item['eth']['dst']), item['eth']['type']))
            # Print out the Packet info
            packet_type = item['packet']['type']
            print('Packet: %s ' % packet_type, end='')
            packet = item['packet']
            if packet_type in ['IP', 'IP6']:
                print('%s --> %s (len:%d ttl:%d)' % (net_utils.inet_to_str(packet['src']), net_utils.inet_to_str(packet['dst']),
                                                     packet['len'], packet['ttl']), end='')
                if packet_type == 'IP':
                    print('-- Frag(df:%d mf:%d offset:%d)' % (packet['df'], packet['mf'], packet['offset']))
                else:
                    print()
            else:
                print(str(packet))
            # Print out transport and application layers
            if item['transport']:
                transport_info = item['transport']
                print('Transport: %s ' % transport_info['type'], end='')
                for key, value in compat.iteritems(transport_info):
                    if key != 'data':
                        print(key+':'+repr(value), end=' ')
                # Give summary info about data
                data = transport_info['data']
                print('\nData: %d bytes' % len(data), end='')
                if data:
                    print('(%s...)' % repr(data)[:30])
                else:
                    print()
            # Application data
            if item['application']:
                print('Application: %s' % item['application']['type'], end='')
                print(str(item['application']))
            # Is there domain info?
            if 'src_domain' in packet:
                print('Domains: %s --> %s' % (packet['src_domain'], packet['dst_domain']))
            # Tags
            if 'tags' in item:
                print(list(item['tags']))
            print()