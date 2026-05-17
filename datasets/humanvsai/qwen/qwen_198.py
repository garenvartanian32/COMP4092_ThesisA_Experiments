def _join_data_lines(lines, skip):
    lines = lines[skip:]
    return b''.join(lines)

def _parse_data(lines, skip):
    """Parse the data lines into a list of dictionaries"""
    lines = lines[skip:]
    data = []
    for line in lines:
        items = line.decode('utf-8').split(',')
        data.append({'item1': items[0], 'item2': items[1], 'item3': items[2]})
    return data

def process_data(lines, skip):
    """Process the data lines into a list of dictionaries and a byte string"""
    byte_data = _join_data_lines(lines, skip)
    parsed_data = _parse_data(lines, skip)
    return (byte_data, parsed_data)
lines = [b'header1,header2,header3\n', b'data1,data2,data3\n', b'data4,data5,data6\n']
skip = 1
(byte_data, parsed_data) = process_data(lines, skip)