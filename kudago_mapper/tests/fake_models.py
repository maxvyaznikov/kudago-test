
class FakeDjangoModel(object):
    """
    This class makes tests easily to go away from django unittests
    infrastructure.
    """


class Event(FakeDjangoModel):
    source_id = None
    has_price = None
    type = None
    title = None
    age_restricted = None
    tags = None
    text = None
