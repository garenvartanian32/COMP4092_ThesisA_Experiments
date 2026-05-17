def print_packet_info(input_stream):
    for packet in input_stream:
        print("Packet Source: {}".format(packet.source))
        print("Packet Destination: {}".format(packet.destination))
        print("Packet Length: {}".format(packet.length))
        print("Packet Data: {}".format(packet.data))
