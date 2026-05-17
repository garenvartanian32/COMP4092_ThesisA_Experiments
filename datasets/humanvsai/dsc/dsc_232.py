def velocity(msg):
    # Convert the hexadecimal message string to binary
    binary_msg = bin(int(msg, 16))[2:].zfill(256)

    # Extract the speed, heading, and vertical rate from the binary message
    speed = int(binary_msg[0:13], 2) * 2  # Convert from kts to kph
    heading = int(binary_msg[13:13+9], 2) * 360 / 512
    vertical_rate = int(binary_msg[13+9:13+9+5], 2) * 32
    speed_type = 'GS' if binary_msg[13+9+5] == '0' else 'AS'

    return speed, heading, vertical_rate, speed_type