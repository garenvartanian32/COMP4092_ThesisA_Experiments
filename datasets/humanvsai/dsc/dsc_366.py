from lxml import etree

def validate_metadata(self, xml):
    # Load the XML
    try:
        xml_tree = etree.fromstring(xml)
    except etree.XMLSyntaxError as e:
        return [f"Invalid XML: {e}"]

    # Load the schema
    try:
        with open('schema.xsd', 'r') as schema_file:
            schema = etree.XMLSchema(etree.parse(schema_file))
    except etree.XMLSchemaError as e:
        return [f"Invalid schema: {e}"]

    # Validate the XML
    if not schema.validate(xml_tree):
        return [f"Invalid metadata: {schema.error_log}"]

    return []