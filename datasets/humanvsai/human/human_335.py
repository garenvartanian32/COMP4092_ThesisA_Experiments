def list(self):
        params = {'user': self.user_id}
        response = self.session.get(self.url, params=params)
        blocks = response.data['blocks']
        return [Block(self, **block) for block in blocks]