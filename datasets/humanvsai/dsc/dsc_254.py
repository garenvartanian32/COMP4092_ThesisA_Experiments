import json

class Team:
    def __init__(self):
        self.roster = [
            {"name": "John", "position": "Point Guard"},
            {"name": "Jane", "position": "Shooting Guard"},
            {"name": "Joe", "position": "Small Forward"},
            {"name": "Jill", "position": "Power Forward"},
            {"name": "Jim", "position": "Center"}
        ]

    def get_teams(self):
        return json.dumps(self.roster)

team = Team()
print(team.get_teams())