def to_xml(self):
    '''Serialises the FoLiA element to XML, by returning an XML Element 
    (in lxml.etree) for this element and all its children. For string 
    output, consider the xmlstring() method instead.
    '''
    return self._element
