def block_anyfilter(parser, token):
    nodelist = parser.parse(('endblockanyfilter',))
    parser.delete_first_token()
    filter_func = token.split_contents()[1]
    args = token.split_contents()[2:]
    return BlockAnyFilterNode(nodelist, filter_func, args)

class BlockAnyFilterNode(template.Node):

    def __init__(self, nodelist, filter_func, args):
        self.nodelist = nodelist
        self.filter_func = filter_func
        self.args = args

    def render(self, context):
        output = self.nodelist.render(context)
        filter_func = getattr(django.template.defaultfilters, self.filter_func)
        args = [output] + [context.get(arg) for arg in self.args]
        return filter_func(*args)