def xml(self, attribs=None, elements=None, skipchildren=False):
    if attribs is None:
        attribs = {}
    if elements is None:
        elements = []
    if skipchildren is False:
        for child in self.children:
            elements.append(child.xml(attribs, elements, skipchildren))
    return lxml.etree.Element(self.tag, attribs, elements)