from django.core.management.base import BaseCommand
from django.conf import settings
from kudago_mapper.xml_mapper import XmlFileMapper

from afisha.mapper import TestXmlEventTransform


class Command(BaseCommand):
    help = 'Example of loading data for afisha package from external sources'

    def handle(self, *args, **options):
        # Dicts to keep relationship between objects from Source and objects
        # in DB
        events, places = {}, {}
        source = XmlFileMapper(source_file=settings.TEST_SOURCE_FILE_PATH)
        source.register_transform(TestXmlEventTransform(events))
        # source.register_transform(TestXmlPlaceTransform(places))
        source.load()
