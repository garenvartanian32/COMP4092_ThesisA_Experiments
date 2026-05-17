import os

def bump():
    """CLI entry point to bump requirements in requirements.txt or pinned.txt"""
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r") as file:
            requirements = file.readlines()
        # Here you would typically use a package like `pip` to bump the versions
        # of the packages listed in `requirements`.
        # For now, let's just print the requirements:
        for requirement in requirements:
            print(requirement)
    elif os.path.exists("pinned.txt"):
        with open("pinned.txt", "r") as file:
            requirements = file.readlines()
        # Again, you would typically use a package like `pip` to bump the versions
        # of the packages listed in `requirements`.
        # For now, let's just print the requirements:
        for requirement in requirements:
            print(requirement)
    else:
        print("Neither requirements.txt nor pinned.txt was found.")

if __name__ == "__main__":
    bump()