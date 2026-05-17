class User:
    def __init__(self, username):
        self.username = username

    def change_username(self, new_username):
        self.username = new_username
        print(f"Username changed to {self.username}")

# Create a new user
user = User('old_username')

# Change the username
user.change_username('new_username')