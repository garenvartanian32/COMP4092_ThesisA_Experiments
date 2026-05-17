def _read_points(self, vlrs):
    point_format = self.header.point_format
    number_of_points = self.header.number_of_points
    points = []
    laszip_vlr = next((vlr for vlr in vlrs if vlr.record_id == 34735), None)
    if laszip_vlr:
        pass
    else:
        with open(self.file_path, 'rb') as file:
            file.seek(self.header.offset_to_point_data)
            points_data = file.read(number_of_points * self.header.point_record_length)
            for i in range(number_of_points):
                point_data = points_data[i * self.header.point_record_length:(i + 1) * self.header.point_record_length]
                point = self._parse_point(point_data, point_format)
                points.append(point)
    return points

def _parse_point(self, point_data, point_format):
    """private function to parse a single point record from the point data.

        the point format determines the structure of the point record"""
    if point_format == 0:
        format_string = '<3i2H'
    elif point_format == 1:
        format_string = '<3i2H2B'
    elif point_format == 2:
        format_string = '<3i2H2B2H'
    elif point_format == 3:
        format_string = '<3i2H2B2H2H'