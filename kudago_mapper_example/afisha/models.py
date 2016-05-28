from django.db import models
from django.utils.translation import gettext as _


class Event(models.Model):
    external_id = models.CharField(max_length=256)
    has_price = models.BooleanField()
    type = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    age_restricted = models.CharField(max_length=3, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    stage_theatre = models.CharField(max_length=256, blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def tags_admintag(self):
        return ', '.join([tag.name for tag in self.tags.order_by('name')])
    tags_admintag.short_description = _('Tags')
    tags_admintag.allow_tags = True


class Place(models.Model):
    external_id = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    address = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    phones = models.TextField(blank=True, null=True)
    work_time = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    metro = models.ManyToManyField('Metro')

    def __str__(self):
        return self.title

    def metro_admintag(self):
        return ', '.join([metro.name for metro in self.metro.order_by('name')])
    metro_admintag.short_description = _('Metro')
    metro_admintag.allow_tags = True

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Metro(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.url


class EventImage(Image):
    event = models.ForeignKey('Event')


class PlaceImage(Image):
    place = models.ForeignKey('Place')


class Session(models.Model):
    date = models.DateField()
    event = models.ForeignKey('Event')
    place = models.ForeignKey('Place')
    time = models.CharField(max_length=5)
    time_till = models.CharField(max_length=5, blank=True, null=True)
