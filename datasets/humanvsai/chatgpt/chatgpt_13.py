import json
import yaml
from io import StringIO

def convert_format(input_file=None, output_file=None, output_format='json'):
    if input_file is None:
        input_file = StringIO(input())
    if output_format == 'json':
        data = yaml.load(input_file, Loader=yaml.FullLoader)
        output_string = json.dumps(data)
    elif output_format == 'properties':
        pass # Implement conversion to properties format
    elif output_format == 'yaml':
        data = json.loads(input_file.read())
        output_string = yaml.dump(data, default_flow_style=False)
    else:
        raise ValueError("Invalid output format. Supported formats are 'json', 'properties', and 'yaml'.")
    
    if output_file is None:
        print(output_string)
    else:
        with open(output_file, 'w') as file:
            file.write(output_string)
