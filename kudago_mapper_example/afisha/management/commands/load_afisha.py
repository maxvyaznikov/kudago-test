from django.core.management.base import BaseCommand
from django.conf import settings
from kudago_mapper.xml_mapper import XmlFileMapper

from afisha.mapper.test_xml.event_mapper import TestXmlEventTransform
from afisha.models import Event, Place


class Command(BaseCommand):
    help = 'Example of loading data for afisha package from external sources'

    def handle(self, *args, **options):
        # Dicts to keep relationship between objects from external source and
        # objects in DB
        events = {event.external_id: event for event in Event.objects.all()}
        places = {place.external_id: place for place in Place.objects.all()}
        source = XmlFileMapper(source_file=settings.TEST_SOURCE_FILE_PATH)
        source.register_transform(TestXmlEventTransform(events))
        # source.register_transform(TestXmlPlaceTransform(places))
        source.load()
