import logging
from lxml import etree

from kudago_mapper.base import MapperBase, TransformBase


class XmlFileMapper(MapperBase):
    """
    Data mapper to load data from XML-file and convert by using registered
    data transforms
    """
    source_file = None

    def __init__(self, source_file):
        self.source_file = source_file

    def load(self):
        """
        Load data from source and try to convert each element
        """
        context = etree.iterparse(self.source_file,
                                  events=('start',),
                                  remove_blank_text=True,
                                  remove_comments=True)
        for event, element in context:
            self.do_convert(element)

    def get_element_type(self, element):
        """
        Type getter from XML-element

        :param element: XML-element
        :type element: lxml->Element object
        :return: Type of element to find existing transform for this element
        :rtype: string
        """
        return element.tag


class XmlTransform(TransformBase):
    """
    Data transform class to help convert elements from XML-file
    """
    logger = logging.getLogger(__name__ + '.' + __qualname__)

    def convert_element(self, element):
        for child in element.iterchildren():
            try:
                fn = getattr(self, 'convert_child_' + child.tag)
            except AttributeError:
                self.logger.warning('{}->{} conversion was '
                                    'missed'.format(element.tag, child.tag))
            else:
                fn(child)
