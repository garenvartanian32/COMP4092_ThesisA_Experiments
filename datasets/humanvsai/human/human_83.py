def pre_order(root):
        # type: (Nonterminal) -> Generator
        def traverse_rule(item, callback):
            yield item
            for el in item.to_symbols:
                yield callback(el)
        def traverse_nonterminal(item, callback):
            yield item
            yield callback(item.to_rule)
        def traverse_terminal(item, callback):
            yield item
        return Traversing.traverse_separated(root, traverse_rule, traverse_nonterminal, traverse_terminal)