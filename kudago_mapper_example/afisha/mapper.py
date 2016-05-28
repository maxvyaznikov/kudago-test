from kudago_mapper.base import TransformBase

from afisha.models import Event, Place, Tag, Metro, Image


class TestXmlEventTransform(TransformBase):
    element_type = 'event'
    events = None

    def __init__(self, events):
        self.events = events

    def convert_element(self, element):
        self.event = Event()
        # Extract data from tag attributes
        self.event.external_id = int(element.get('id'))
        self.event.has_price = element.get('price', True)
        self.event.type = element.get('type')
        # Extract data from children
        super().convert_element(element)
        # Save in DB
        self.event.save()
        # Save in global dict relationship between Source ID and Database ID
        self.events[self.event.external_id] = self.event.id

    def convert_child_title(self, child):
        self.event.title = child.text

    def convert_child_age_restricted(self, child):
        self.event.age_restricted = child.text

    def convert_child_text(self, child):
        self.event.text = child.text

    # def convert_child_tags(self, child):
    #     self.event.tags = [tag.text for tag in child.iterchildren()]
