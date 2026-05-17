class MyClass:
    def __init__(self):
        self.triggers = {
            ("scope1", "name1"): ("trigger1", "trigger2"),
            ("scope2", "name2"): ("trigger3", "trigger4"),
            # add more scopes and names as needed
        }

    def getTriggerStrings(self, parScope, parName):
        """For a given item (scope + name), return all strings (in a tuple)
        that it is meant to trigger, if any exist.  Returns None is none."""
        return self.triggers.get((parScope, parName))