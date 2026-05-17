from lxml import etree

class FoLiA:
    def __init__(self, attribs=None, elements=None):
        self.attribs = attribs or {}
        self.elements = elements or []

    def xml(self, skipchildren=False):
        element = etree.Element('FoLiA', self.attribs)

        if not skipchildren:
            for child in self.elements:
                element.append(child.xml())

        return element