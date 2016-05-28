from lxml import etree

from kudago_mapper.base import MapperBase


class XmlFileMapper(MapperBase):
    """

    """
    source_file = None

    def __init__(self, source_file):
        self.source_file = source_file

    def load(self):
        """

        """
        context = etree.iterparse(self.source_file,
                                  events=('start',),
                                  remove_blank_text=True,
                                  remove_comments=True)
        for event, element in context:
            self.do_convert(element)

    def get_element_type(self, element):
        return element.tag

