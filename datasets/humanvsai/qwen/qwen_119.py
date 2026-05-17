def get_stories(self, *args, **kwargs):
    url = f'{self.base_url}/creators/{self.creator_id}/stories'
    params = self._get_params(*args, **kwargs)
    response = self._make_request(url, params=params)
    return StoriesDataWrapper(response.json())

class StoriesDataWrapper:

    def __init__(self, data):
        self.data = data

    def get_story_ids(self):
        """Returns a list of story IDs from the data."""
        return [story['id'] for story in self.data['stories']]

    def get_story_titles(self):
        """Returns a list of story titles from the data."""
        return [story['title'] for story in self.data['stories']]

    def get_story_details(self, story_id):
        """Returns details of a specific story by its ID."""
        for story in self.data['stories']:
            if story['id'] == story_id:
                return story
        return None