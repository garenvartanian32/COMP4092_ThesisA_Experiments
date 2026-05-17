def _nbaSeason(year):
    """Takes in 4-digit year for first half of season and returns API appropriate formatted code

    Input Values: YYYY 

    Used in: _Draft.Anthro(), _Draft.Agility(), _Draft.NonStationaryShooting(), 
    _Draft.SpotUpShooting(), _Draft.Combine()"""

    # Check if the input is a 4-digit number
    if isinstance(year, int) and 1000 <= year <= 9999:
        # Format the year as a string
        formatted_year = str(year)
        return formatted_year
    else:
        raise ValueError("Input must be a 4-digit year")