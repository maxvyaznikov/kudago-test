import logging


class MapperBase(object):
    _transforms = {}

    def register_transform(self, mapper):
        self._transforms[mapper.element_type] = mapper

    def load(self):
        raise NotImplementedError('Override `load` method to load data from '
                                  'source')

    def get_element_type(self, element):
        """
        Override this function to say how to get name of element

        :param element: Element from some source with data to convert
        :type element: Any object from source
        :return: Name of element
        :rtype: string
        """
        raise NotImplementedError('Override `get_element_type` method to make '
                                  'possible to find mapper for element by '
                                  'it\'s type')

    def do_convert(self, element):
        """
        Find mapper and call function to process an element

        :param element: Element from some source with data to convert
        :type element: Any object from source
        :return: Nothing
        """
        element_type = self.get_element_type(element)
        if element_type in self._transforms:
            self._transforms[element_type].convert_element(element)


class TransformBase(object):
    # Name of element to bind to.
    element_type = None
    logger = logging.getLogger(__name__ + '.' + __qualname__)

    def convert_element(self, element):
        # Override this function and place your code here
        for child in element.iterchildren():
            try:
                getattr(self, 'convert_child_' + child.tag)(child)
            except AttributeError:
                self.logger.warning('{}->{} conversion was '
                                    'missed'.format(element.tag, child.tag))
