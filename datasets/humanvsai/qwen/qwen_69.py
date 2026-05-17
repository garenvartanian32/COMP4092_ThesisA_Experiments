def activities(self):
    return self.client.get_activities(club_id=self.id, limit=100)