def write_ioc(root, output_dir=None, force=False):
    import os
    import xml.etree.ElementTree as ET
    if not force and root.tag != 'OpenIOC':
        raise ValueError("Root element must be 'OpenIOC'")
    if output_dir is None:
        output_dir = os.getcwd()
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, 'output.ioc')
    try:
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f'An error occurred while writing the IOC: {e}')
        return False