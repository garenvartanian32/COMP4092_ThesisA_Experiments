def delete(self):
    response = self.session.delete(self.url)
    if response.status_code == 204:
        return True
    else:
        return False