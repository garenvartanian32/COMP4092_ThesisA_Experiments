def removeAccount(self, account):
    if account in self.accounts:
        del self.accounts[account]
        print(f'Account {account} removed successfully.')
    else:
        print(f'Account {account} not found.')