import struct

def modify_pkt_os(pkt, osdetails=None, osgenre=None, signature=None):

    TCP_HEADER_LENGTH = 20

    # p0f OS Signature table
    OS_SIGNATURES = {
        'Windows': (b'\x00\x02\x5e\x10\x02\x40\x01\x00\x80\x01\x00\x00\xaa\x00\x00\x00',
                    b'\xff\xff\xff\x00'),
        'Linux': (b'\x01\x03\x6d\xc1\x04\x02\x80\x31\x00\x00\x40\x02\xaa\xaa\x00\x00',
                  b'\xff\xff\xff\x00'),
        'FreeBSD': (b'\x01\x02\xf7\x10\x02\x04\x02\x00\x00\x00\x40\x01\x00\x00\x00\x00',
                    b'\xff\xff\xff\x00'),
        # Add more signatures here
    }

    # If signature is provided, use that
    if signature:
        os_sig, os_mask = signature
    # If osdetails is provided, use that to lookup signature in OS_SIGNATURES
    elif osdetails and osdetails in OS_SIGNATURES:
        os_sig, os_mask = OS_SIGNATURES[osdetails]
    # If osgenre is provided, randomly pick personality matching osgenre
    elif osgenre and osgenre in OS_SIGNATURES:
        os_sigs = OS_SIGNATURES[osgenre]
        os_sig, os_mask = os_sigs[random.randint(0, len(os_sigs) - 1)]
    # Else, use a local signature
    else:
        # Implement function to get local signature
        os_sig, os_mask = p0f_getlocalsigs()

    # Extract relevant fields from TCP header
    # https://en.wikipedia.org/wiki/IPv4#Header
    ip_header_length = (pkt[0] & 0xf) * 4
    tcp_header_length = (pkt[ip_header_length + 12] >> 4) * 4

    # Calculate TCP Sequence Number and Acknowledgement Number
    seq_num_raw = pkt[ip_header_length + tcp_header_length + 4:ip_header_length + tcp_header_length + 8]
    seq_num = struct.unpack('!L', seq_num_raw)[0]
    ack_num_raw = pkt[ip_header_length + tcp_header_length + 8:ip_header_length + tcp_header_length + 12]
    ack_num = struct.unpack('!L', ack_num_raw)[0]

    # Modify packet to match os_sig and os_mask
    pkt = bytearray(pkt)
    pkt[ip_header_length + tcp_header_length + 2] = 0x40
    pkt[ip_header_length + tcp_header_length + 16:ip_header_length + tcp_header_length + 20] = os_sig
    pkt[ip_header_length + tcp_header_length + 20:ip_header_length + tcp_header_length + 24] = os_mask

    # Recalculate IP and TCP checksums
    # This step requires OS X and Linux (tested on Ubuntu 16.04 LTS)
    # It may not work with other operating systems or versions
    # If it doesn't work, try using the scapy library to recalculate the checksums
    pkt[ip_header_length + 10:ip_header_length + 12] = b'\x00\x00'
    pkt[ip_header_length + 24:ip_header_length + 26] = b'\x00\x00'
    pseudo_header = struct.pack('!4s4sBBH', pkt[12:16], pkt[16:20], 0, 6, len(pkt) - ip_header_length)
    tcp_header = pkt[ip_header_length:ip_header_length + tcp_header_length]
    tcp_checksum_data = pseudo_header + tcp_header + pkt[ip_header_length + tcp_header_length:]
    tcp_checksum = checksum(tcp_checksum_data)
    pkt[ip_header_length + 16:ip_header_length + 18] = struct.pack('!H', tcp_checksum)

    return pkt
