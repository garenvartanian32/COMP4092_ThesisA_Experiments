def bump():
    import sys
    import subprocess
    import os
    if len(sys.argv) != 2:
        print('Usage: bump <requirements.txt or pinned.txt>')
        sys.exit(1)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f'Error: {filename} does not exist.')
        sys.exit(1)
    if filename not in ['requirements.txt', 'pinned.txt']:
        print('Error: Only requirements.txt or pinned.txt are allowed.')
        sys.exit(1)
    with open(filename, 'r') as file:
        lines = file.readlines()
    bumped_lines = []
    for line in lines:
        if line.strip() and (not line.startswith('#')):
            (package, version) = line.split('==')
            new_version = bump_version(version.strip())
            bumped_lines.append(f'{package}=={new_version}\n')
        else:
            bumped_lines.append(line)
    with open(filename, 'w') as file:
        file.writelines(bumped_lines)
    print(f'Versions in {filename} have been bumped.')

def bump_version(version):
    """Bump the version number by incrementing the patch version."""
    (major, minor, patch) = map(int, version.split('.'))
    new_patch = patch + 1
    return f'{major}.{minor}.{new_patch}'