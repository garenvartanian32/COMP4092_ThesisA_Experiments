def removeAccount(self, account):
    """Remove all keys associated with a given account"""
    if account in self.accounts:
        del self.accounts[account]