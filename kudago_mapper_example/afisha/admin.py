from django.contrib import admin

from afisha.models import Event, Place, Session


class EventAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'has_price', 'type', 'title',
                    'age_restricted', 'tags_admintag')
    ordering = ('title',)

admin.site.register(Event, EventAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'city', 'title', 'address', 'url',
                    'metro_admintag')
    ordering = ('title',)

admin.site.register(Place, PlaceAdmin)


class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'event', 'place', 'time', 'time_till')
    ordering = ('date',)
    date_hierarchy = 'date'

admin.site.register(Session, SessionAdmin)
