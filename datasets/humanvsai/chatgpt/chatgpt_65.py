import os
from sphinx.ext import autodoc

def create_rst_files(in_dir):
    for root, dirs, files in os.walk(in_dir):
        for file in files:
            if file.endswith('.py'):
                module_path = os.path.join(root, file).replace('/', '.')[:-3]
                with open(os.path.join(root, file.rsplit('.')[0] + '.rst'), 'w') as f:
                    f.write(module_path + '\n')
                    f.write('=' * len(module_path) + '\n\n')
                    f.write('.. automodule:: {}\n'.format(module_path))
                    f.write('    :members:\n')
                    f.write('    :undoc-members:\n')
                    f.write('    :show-inheritance:\n')
                    f.write('    :private-members:\n')
                    f.write('    :special-members: __repr__\n\n')
