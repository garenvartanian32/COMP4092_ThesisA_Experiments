import argparse

def add_arguments(argument_group):
    argument_group.add_argument('--arg1', help='Help message for arg1')
    argument_group.add_argument('--arg2', default='default_value', help='Help message for arg2')
    argument_group.add_argument('--arg3', type=int, help='Help message for arg3')
    # Add more arguments as needed
