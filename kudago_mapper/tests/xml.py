from unittest import TestCase

from kudago_mapper.base import TransformBase
from kudago_mapper.xml import XmlFileMapper
from kudago_mapper.tests.fake_models import Event


class TestXmlEventTransform(TransformBase):
    element_type = 'event'
    events = None

    def __init__(self, events):
        self.events = events

    def convert_element(self, element):
        self.event = Event()
        self.event.external_id = int(element.get('id'))
        self.event.has_price = element.get('price', True)
        self.event.type = element.get('type')
        super().convert_element(element)
        self.events[self.event.external_id] = self.event

    def convert_child_title(self, child):
        self.event.title = child.text

    def convert_child_age_restricted(self, child):
        self.event.age_restricted = child.text

    def convert_child_text(self, child):
        self.event.text = child.text

    def convert_child_tags(self, child):
        self.event.tags = [tag.text for tag in child.iterchildren()]



class TestMapper(TestCase):

    def test_event_model_creation(self):
        events = {}
        source = XmlFileMapper(source_file='test_source.xml')
        source.register_transform(TestXmlEventTransform(events))
        source.load()

        event = events[93822]
        self.assertEqual(event.title, 'Дао')
        self.assertEqual(event.age_restricted, '16+')
