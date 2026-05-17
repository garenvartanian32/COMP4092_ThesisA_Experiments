def pass_actualremoterelease_v1(self):
    flu = self.sequences.fluxes.fastaccess
    out = self.sequences.outlets.fastaccess
    out.s[0] += flu.actualremoterelease