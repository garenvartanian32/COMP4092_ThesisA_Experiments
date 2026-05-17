def validate_metadata(self, xml):
    errors = []
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as e:
        errors.append(f'XML parsing error: {e}')
        return errors
    required_elements = ['EntityDescriptor', 'SPSSODescriptor', 'AssertionConsumerService']
    for element in required_elements:
        if root.find(f'.//{element}') is None:
            errors.append(f'Missing required element: {element}')
    required_attributes = {'EntityDescriptor': ['entityID'], 'SPSSODescriptor': ['protocolSupportEnumeration'], 'AssertionConsumerService': ['Binding', 'Location']}
    for (element, attributes) in required_attributes.items():
        found_element = root.find(f'.//{element}')
        if found_element is not None:
            for attribute in attributes:
                if found_element.get(attribute) is None:
                    errors.append(f'Missing required attribute {attribute} in element {element}')
    spsso_descriptor = root.find('.//SPSSODescriptor')
    if spsso_descriptor is not None:
        protocol_support = spsso_descriptor.get('protocolSupportEnumeration')
        if protocol_support != 'urn:oasis:names:tc:SAML:2.0:protocol':
            errors.append('Invalid protocolSupportEnumeration value in SPSSODescriptor')
    return errors