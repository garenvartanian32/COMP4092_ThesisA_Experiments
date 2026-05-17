def get_teams(self):
        return self.make_request(host="erikberg.com", sport='nba',
                                 method="teams", id=None,
                                 format="json",
                                 parameters={})