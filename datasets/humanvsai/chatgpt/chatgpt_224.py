import os
import lxml.etree as etree

def serialize_ioc(root, output_dir=os.getcwd(), force=False):
    if not force and root.tag != 'OpenIOC':
        raise ValueError('Root element must have tag "OpenIOC"')
        
    filename = os.path.join(output_dir, root.get('id', 'untitled.ioc'))
    
    with open(filename, 'wb') as f:
        f.write(etree.tostring(root, pretty_print=True))
    
    return True
