def get_teams(self):
    response = self.session.get(self.base_url + '/teams')
    response.raise_for_status()
    return response.json()

def get_players(self):
    """Return json current roster of players"""
    response = self.session.get(self.base_url + '/players')
    response.raise_for_status()
    return response.json()

def get_coaches(self):
    """Return json current roster of coaches"""
    response = self.session.get(self.base_url + '/coaches')
    response.raise_for_status()
    return response.json()

def get_games(self):
    """Return json current schedule of games"""
    response = self.session.get(self.base_url + '/games')
    response.raise_for_status()
    return response.json()

def get_standings(self):
    """Return json current standings of teams"""
    response = self.session.get(self.base_url + '/standings')
    response.raise_for_status()
    return response.json()

def get_stats(self):
    """Return json current stats of players"""
    response = self.session.get(self.base_url + '/stats')
    response.raise_for_status()
    return response.json()