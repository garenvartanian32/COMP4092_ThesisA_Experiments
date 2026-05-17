def _read_points(self, vlrs):
        try:
            extra_dims = vlrs.get("ExtraBytesVlr")[0].type_of_extra_dims()
        except IndexError:
            extra_dims = None
        point_format = PointFormat(self.header.point_format_id, extra_dims=extra_dims)
        if self.header.are_points_compressed:
            laszip_vlr = vlrs.pop(vlrs.index("LasZipVlr"))
            points = self._read_compressed_points_data(laszip_vlr, point_format)
        else:
            points = record.PackedPointRecord.from_stream(
                self.stream, point_format, self.header.point_count
            )
        return points