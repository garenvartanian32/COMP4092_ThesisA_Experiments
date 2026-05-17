import argparse

def bump_requirements():
    parser = argparse.ArgumentParser(description='CLI entry point to bump requirements in requirements.txt or pinned.txt')
    parser.add_argument('filename', type=str, help='name of the file to bump requirements in')
    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        lines = f.readlines()

    with open(args.filename, 'w') as f:
        for line in lines:
            if line.startswith('requirements=='):
                _, version = line.strip().split('==')
                new_version = str(int(version) + 1)
                f.write(f'requirements=={new_version}\n')
            else:
                f.write(line)

if __name__ == '__main__':
    bump_requirements()
