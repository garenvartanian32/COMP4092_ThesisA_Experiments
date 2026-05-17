def getTriggerStrings(self, parScope, parName):
        # The data structure of _allTriggers was chosen for how easily/quickly
        # this particular access can be made here.
        fullName = parScope+'.'+parName
        return self._allTriggers.get(fullName)