
# register this as documented at
#   http://collective-docs.readthedocs.org/en/latest/searching_and_indexing/indexing.html#custom-index-methods


from plone.indexer.decorator import indexer
from Products.ATContentTypes.interfaces.event import IATEvent
from Products.ATContentTypes.utils import DT2dt


@indexer(IATEvent)
def event_days(context, **kw):
    start = DT2dt(context.getStartDate())
    end = DT2dt(context.getEndDate())
    delta = end - start
    return delta.days
