def _read_points_record_parts(header, vlrs):
    # Code to handle reading of the points record parts
    # of the las file using the header and vlrs arguments
    
    # Get the point format and number of points from the header
    point_format = header.point_format
    num_points = header.number_of_points
    
    # Get the potential laszip vlr and the extra bytes vlr from the vlrs
    laszip_vlr = None
    extra_bytes_vlr = None
    for vlr in vlrs:
        if vlr.user_id == 22204:
            laszip_vlr = vlr
        elif vlr.user_id == 4:
            extra_bytes_vlr = vlr
    
    # Return the obtained values
    return point_format, num_points, laszip_vlr, extra_bytes_vlr
