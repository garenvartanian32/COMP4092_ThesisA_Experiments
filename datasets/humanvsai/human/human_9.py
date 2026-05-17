def block_anyfilter(parser, token):
    bits = token.contents.split()
    nodelist = parser.parse(('endblockanyfilter',))
    parser.delete_first_token()
    return BlockAnyFilterNode(nodelist, bits[1], *bits[2:])