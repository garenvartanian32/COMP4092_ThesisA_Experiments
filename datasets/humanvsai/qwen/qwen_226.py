def pull(self):
    for packet in self.input_stream:
        print(packet)

def push(self, packet):
    """Add a packet to the output_stream"""
    self.output_stream.append(packet)

def process(self):
    """Process packets from input_stream and send them to output_stream"""
    for packet in self.input_stream:
        self.push(packet)