def velocity(msg):
    speed_type = msg[26:28]
    speed = int(msg[24:26], 16)
    heading = int(msg[28:32], 16) / 1024.0 * 360.0
    vertical_rate = int(msg[32:36], 16) * 64
    if speed_type == '01':
        speed_type = 'GS'
    elif speed_type == '02':
        speed_type = 'AS'
    else:
        speed_type = 'Unknown'
    return (speed, heading, vertical_rate, speed_type)
msg = '0000000000000000000000000000000000000000000000000000000000000000'