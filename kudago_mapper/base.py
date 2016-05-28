

class MapperBase(object):
    """
    Interface for data mappers with methods to load data, register objects to
    make transformations of data and other
    """
    # Keep transforms in one dict as {element_type: transform object}
    _transforms = {}

    def register_transform(self, mapper):
        if not mapper.element_type:
            raise ValueError('Mapper to transform data must have '
                             '`element_type` specified')
        self._transforms[mapper.element_type] = mapper

    def load(self):
        """
        Override this method to load data from sources

        :return: None
        """
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
    """
    Data transform class to help convert elements from external source
    """
    element_type = None  # Type of element to bind this data transform to
