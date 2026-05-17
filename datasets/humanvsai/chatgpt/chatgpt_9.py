from django.template.base import TemplateSyntaxError
from django.template.defaulttags import BlockNode, TextNode
from django.template.defaultfilters import stringfilter
from django.template.library import parse_bits
from django.utils.safestring import mark_safe

from django import template


register = template.Library()


def block_anyfilter(parser, token):
    """
    Turns any template filter into a blocktag. Usage:

    {% load libs_tags %}
    {% block_anyfilter django.template.defaultfilters.truncatewords_html 15 %}
        // Something complex that generates html output
    {% endblock_anyfilter %}
    """
    bits = token.split_contents()
    if len(bits) < 3:
        raise TemplateSyntaxError("'%s' takes at least two arguments (function name and number of words)" % bits[0])
    filter_string = bits[1]
    if not filter_string.startswith('django.template.defaultfilters.'):
        raise TemplateSyntaxError("'%s' is not a valid filter function name")
    varbits, argbits, argnames, defaults = parse_bits(parser, bits[2:], [], [], None, None)
    nodelist = parser.parse(('endblock_anyfilter',))
    parser.delete_first_token()
    return AnyFilterNode(filter_string, varbits, argbits, argnames, defaults, nodelist)


class AnyFilterNode(BlockNode):
    def __init__(self, filter_string, varbits, argbits, argnames, defaults, nodelist):
        self.filter_string = filter_string
        self.varbits = varbits
        self.argbits = argbits
        self.argnames = argnames
        self.defaults = defaults
        self.nodelist = nodelist

    def render(self, context):
        filter_func = template.Variable(self.filter_string).resolve(context)
        filter_args = []
        filter_kwargs = {}
        for i, bit in enumerate(self.argbits):
            value = bit.resolve(context)
            if self.defaults is not None and value == self.defaults[i]:
                continue
            if self.argnames and isinstance(self.argnames[i], str):
                filter_kwargs[self.argnames[i]] = value
            else:
                filter_args.append(value)
        output = self.nodelist.render(context)
        output = filter_func(output, *filter_args, **filter_kwargs)
        return mark_safe(output)

    def super(self):
        return super().as_text()


register.tag('block_anyfilter', block_anyfilter)
