from django.db import models


class Event(models.Model):
    external_id = models.CharField(max_length=256)
    has_price = models.BooleanField()
    type = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    age_restricted = models.CharField(max_length=3, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag')
    metro = models.ManyToManyField('Metro')


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


class Tag(models.Model):
    name = models.CharField(max_length=256)


class Metro(models.Model):
    name = models.CharField(max_length=256)


class Image(models.Model):
    url = models.TextField()

    class Meta:
        abstract = True


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
