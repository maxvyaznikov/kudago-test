"""
Tests file for `kudago_mapper.xml_mapper.XmlFileMapper` class
"""
from unittest import TestCase

from kudago_mapper.xml_mapper import XmlFileMapper, XmlTransform
from kudago_mapper.tests.fake_models import Event


class TestXmlEventTransform(XmlTransform):
    element_type = 'event'
    events = None

    def __init__(self, events):
        self.events = events

    def convert_element(self, element):
        self.event = Event()
        self.event.external_id = element.get('id')
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



class TestXmlFileMapper(TestCase):

    def _load_xml_file(self, file_name, **kwargs):
        source = XmlFileMapper(source_file=file_name)
        source.register_transform(TestXmlEventTransform(**kwargs))
        source.load()

    def test_source_simple(self):
        events = {}
        self._load_xml_file('test_source_simple.xml', events=events)

        event = events['93492']
        self.assertEqual(event.title, 'Kodaline')
        self.assertEqual(event.age_restricted, '18+')
        self.assertEqual(event.text, None)
        self.assertTrue(event.has_price)
        self.assertEqual(event.type, 'concert')
        self.assertListEqual(event.tags, ['18+', 'концерт', 'рок и рок-н-ролл'])

    def test_source_with_long_nested_structure(self):
        events = {}
        self._load_xml_file('test_source_with_long_nested_structure.xml', events=events)

        event = events['123']
        self.assertEqual(event.title, 'Дао')
