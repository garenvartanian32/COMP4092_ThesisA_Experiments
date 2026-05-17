def AddArguments(cls, argument_group):
    argument_group.add_argument('--input', type=str, help='Input file path')
    argument_group.add_argument('--output', type=str, help='Output file path')
    argument_group.add_argument('--verbose', action='store_true', help='Enable verbose mode')
    argument_group.add_argument('--debug', action='store_true', help='Enable debug mode')

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Process some files.')
    AddArguments(parser)
    args = parser.parse_args()
    print(args)