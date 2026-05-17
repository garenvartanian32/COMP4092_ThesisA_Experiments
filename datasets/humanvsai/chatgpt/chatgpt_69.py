from stravalib.client import Client

def club_activities(club_id):
    client = Client()
    activities = client.get_club_activities(club_id)
    for activity in reversed(list(activities)):
        yield activity
