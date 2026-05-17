def getTriggerStrings(self, parScope, parName):
    if (parScope, parName) in self.triggerDict:
        return self.triggerDict[parScope, parName]
    else:
        return None