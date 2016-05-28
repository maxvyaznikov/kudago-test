"""
Tests file for `kudago_mapper.xml_mapper.XmlTransform` class
"""
from unittest import TestCase
from lxml import etree

from kudago_mapper.xml_mapper import XmlTransform


class TestConversionCallTransform(XmlTransform):
    was_conversion_called = False

    def convert_child_small_child_of_single_element(self, child):
        self.was_conversion_called = True


class TestXmlTransform(TestCase):

    def test_child_conversion_call(self):
        element = etree.Element('one_single_element')
        element.append(etree.Element('small_child_of_single_element'))
        transform = TestConversionCallTransform()
        self.assertFalse(transform.was_conversion_called)
        transform.convert_element(element)
        self.assertTrue(transform.was_conversion_called)
