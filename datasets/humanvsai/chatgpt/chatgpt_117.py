from everest.querying.base import EXPRESSION_KINDS
from everest.interfaces import IOrderSpecificationVisitor
from zope.component import getUtility

def get_order_specification_visitor_utility(name):
    return getUtility(IOrderSpecificationVisitor, name=name, default=None)
