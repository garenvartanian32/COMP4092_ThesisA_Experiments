def comprehension_walk_newer(self, node, iter_index, code_index=-5):
    if isinstance(node, ast.For):
        target = node.target
        iter = node.iter
        self.comprehension_walk_newer(node.body[0], iter_index + 1, code_index)
        self.process_target(target, iter_index)
        self.process_iter(iter, iter_index)
    elif isinstance(node, ast.If):
        test = node.test
        self.process_test(test, iter_index)
        self.comprehension_walk_newer(node.body[0], iter_index, code_index)
    elif isinstance(node, ast.Expr):
        value = node.value
        self.process_value(value, code_index)
    else:
        raise ValueError('Unsupported node type in comprehension')