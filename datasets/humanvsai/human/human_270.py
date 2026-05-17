def xml(self, attribs = None,elements = None, skipchildren = False):
        E = ElementMaker(namespace=NSFOLIA,nsmap={None: NSFOLIA, 'xml' : "http://www.w3.org/XML/1998/namespace"})
        if not attribs: attribs = {}
        if not elements: elements = []
        if self.id:
            attribs['id'] = self.id
            try:
                w = self.doc[self.id]
                attribs['t'] = w.text()
            except KeyError:
                pass
        e  = makeelement(E, '{' + NSFOLIA + '}' + self.XMLTAG, **attribs)
        return e