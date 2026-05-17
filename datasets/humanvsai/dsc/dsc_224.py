import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element('OpenIOC')

# Add some child elements
child1 = ET.SubElement(root, 'Child1')
child2 = ET.SubElement(root, 'Child2')

# Write the IOC to a file
write_ioc(root, output_dir='/path/to/output/directory')