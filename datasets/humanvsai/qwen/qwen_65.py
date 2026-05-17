def process_directories(self):
    for directory in self.in_dir:
        if os.path.isdir(directory):
            self.process_directory(directory)
        else:
            print(f'Warning: {directory} is not a directory.')
    self.write_index_file()

def process_directory(self, directory):
    """Process a single directory to create rst files."""
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                self.convert_md_to_rst(os.path.join(root, file))
        for dir in dirs:
            self.process_directory(os.path.join(root, dir))

def convert_md_to_rst(self, md_file):
    """Convert a markdown file to an rst file."""
    rst_file = md_file.rsplit('.', 1)[0] + '.rst'
    with open(md_file, 'r', encoding='utf-8') as md:
        md_content = md.read()
    rst_content = markdown_to_rst(md_content)
    with open(rst_file, 'w', encoding='utf-8') as rst:
        rst.write(rst_content)

def markdown_to_rst(self, md_content):
    """Convert markdown content to rst content."""
    return md_content