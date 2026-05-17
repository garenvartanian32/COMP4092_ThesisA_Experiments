class PacketProcessor:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def pull(self):
        for packet in self.input_stream:
            print("Packet information:")
            for key, value in packet.items():
                print(f"{key}: {value}")