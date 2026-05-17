import json

def get_team_roster():
    # code to fetch the current roster of the team in JSON format

    # dummy data
    team_roster = {
        'team_name': 'Example Team',
        'roster': [
            {'name': 'Player 1', 'position': 'Forward'},
            {'name': 'Player 2', 'position': 'Midfielder'},
            {'name': 'Player 3', 'position': 'Defender'},
        ]
    }

    # return the team roster in json format
    return json.dumps(team_roster)
