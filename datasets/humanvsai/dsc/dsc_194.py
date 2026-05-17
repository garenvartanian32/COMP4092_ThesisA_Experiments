def p0f_impersonate(pkt, osgenre=None, osdetails=None, signature=None):
    """
    Modifies pkt so that p0f will think it has been sent by a
    specific OS.  If osdetails is None, then we randomly pick up a
    personality matching osgenre. If osgenre and signature are also None,
    we use a local signature (using p0f_getlocalsigs). If signature is
    specified (as a tuple), we use the signature.

    For now, only TCP Syn packets are supported.
    Some specifications of the p0f.fp file are not (yet) implemented.
    """
    # Your code here