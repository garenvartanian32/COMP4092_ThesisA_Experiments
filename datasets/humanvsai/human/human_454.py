def can_view(self, user=None, access_code=None):
        if user == self.invoice.user:
            return True
        if user.is_staff:
            return True
        if self.invoice.user.attendee.access_code == access_code:
            return True
        return False