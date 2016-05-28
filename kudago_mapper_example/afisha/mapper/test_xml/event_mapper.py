from kudago_mapper.xml_mapper import XmlTransform

from afisha.models import Event, EventImage, Tag, Metro
from afisha.mapper.test_xml import convert_manytomany_children


class TestXmlEventTransform(XmlTransform):
    element_type = 'event'
    events = None
    tags = None  # Cached tags from DB
    metro = None  # Cached metro from DB
    images = None  # Cached images from DB

    def __init__(self, events):
        self.events = events
        self.tags = {tag.name: tag.id for tag in Tag.objects.all()}
        self.metro = {metro.name: metro.id for metro in Metro.objects.all()}
        self.images = {image.url: image.id for image in
                       EventImage.objects.all()}

    def convert_element(self, element):
        # Extract External ID first
        external_id = str(element.get('id'))
        # Find event in cache to update or create a new one
        self.event = self.events.get(external_id) or Event()
        # Extract data from tag attributes
        self.event.external_id = external_id
        self.event.has_price = element.get('price', True)
        self.event.type = element.get('type')
        # Save new event before convert children elements to make possible to
        #  create related objects in DB
        if not self.event.id:
            self.event.save()
        # Extract data from children
        super().convert_element(element)
        # Save in DB after all operations
        self.event.save()
        # Save in global dict relationship between Source ID and Database object
        self.events[self.event.external_id] = self.event

    def convert_child_title(self, child):
        self.event.title = child.text

    def convert_child_age_restricted(self, child):
        self.event.age_restricted = child.text

    def convert_child_text(self, child):
        self.event.text = child.text

    def convert_child_description(self, child):
        self.event.description = child.text

    def convert_child_runtime(self, child):
        self.event.runtime = int(child.text)

    def convert_child_stage_theatre(self, child):
        self.event.stage_theatre = child.text

    def convert_child_tags(self, child):
        self.event.tags = convert_manytomany_children(child, self.tags, Tag)

    def convert_child_metros(self, child):
        self.event.metro = convert_manytomany_children(child, self.metro, Metro)

    def convert_child_gallery(self, child):
        # self.event.event_images_set = \
        #     convert_manytomany_children(child, self.images, EventImage)
        pass
