import re

def regex_from_markers(markers):
    # Escape special characters
    escaped_markers = [re.escape(marker) for marker in markers]
    
    # Join markers with '|' (OR operator)
    regex = '|'.join(escaped_markers)
    
    return regex