def calculate_speed_heading_vertical_rate(msg):
    msg_type = int(msg[0], 16)
    if msg_type == 9 or msg_type == 5 or msg_type == 4:
        tas = int(msg[27] + msg[26], 16)
        if tas == 0:
            return (0, 0.0, 0, 'AS')
        else:
            ground_speed = int(msg[23] + msg[22], 16)
            if ground_speed > 0:
                speed_type = 'GS'
                heading = int(msg[17] + msg[16], 16) * 360.0 / 65536.0
            else:
                speed_type = 'AS'
                heading = int(msg[19] + msg[18], 16) * 360.0 / 65536.0
            vertical_rate = int(msg[25] + msg[24], 16)
            if vertical_rate >= 32767:
                vertical_rate = vertical_rate - 65536
            return (ground_speed, heading, vertical_rate, speed_type)
    else:
        return None