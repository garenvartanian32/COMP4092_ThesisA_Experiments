import lxml.etree as ET

def validate_xml_sp_metadata(xml):
    errors = []
    try:
        schema_doc = ET.parse('public-id://0')
        xmlschema = ET.XMLSchema(schema_doc)
        root = ET.fromstring(xml)
        xmlschema.validate(root)
        return errors
    except ET.XMLSyntaxError as e:
        return [e.message]
    except ET.DocumentInvalid as e:
        for error in xmlschema.error_log:
            errors.append(error.message)
        return errors
