def format_sass_stack(self):
    stack = self.stack
    formatted_stack = []
    for item in stack:
        if isinstance(item, SassImport):
            formatted_stack.append(f'Imported from {item.path}')
        elif isinstance(item, SassMixin):
            formatted_stack.append(f'Mixin called from {item.path}')
        elif isinstance(item, SassFunction):
            formatted_stack.append(f'Function called from {item.path}')
        else:
            formatted_stack.append(f'Unknown item from {item.path}')
    return '\n'.join(formatted_stack)