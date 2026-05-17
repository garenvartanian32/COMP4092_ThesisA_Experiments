def is_member(self, m):
        if not m:
            return False
        elif isinstance(m, basestring):
            jid = m
        else:
            jid = m['JID']
        is_member = len(filter(lambda m: m['JID'] == jid and m.get('STATUS') in ('ACTIVE', 'INVITED'), self.params['MEMBERS'])) > 0
        return is_member