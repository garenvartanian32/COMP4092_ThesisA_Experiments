def generate_catalogue_subparser(subparsers):
    parser = subparsers.add_parser('generate-catalogue', help='Generate and save a catalogue file.')
    parser.add_argument('--output', type=str, required=True, help='The path to the output catalogue file.')
    parser.add_argument('--items', type=str, nargs='+', required=True, help='A list of items to include in the catalogue.')
    parser.add_argument('--format', type=str, choices=['json', 'csv'], default='json', help='The format of the output catalogue file. Default is JSON.')
    return parser

def save_catalogue(output_path, items, file_format):
    """Saves the catalogue to the specified output path in the specified format."""
    if file_format == 'json':
        import json
        with open(output_path, 'w') as f:
            json.dump(items, f, indent=4)
    elif file_format == 'csv':
        import csv
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Item'])
            for item in items:
                writer.writerow([item])
    else:
        raise ValueError(f'Unsupported file format: {file_format}')

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Catalogue Generator')
    subparsers = parser.add_subparsers(dest='command')
    generate_catalogue_subparser(subparsers)
    args = parser.parse_args()
    if args.command == 'generate-catalogue':
        save_catalogue(args.output, args.items, args.format)