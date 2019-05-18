from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'event_start', 'event_end', 'event_address')
	list_display_links = ('event_name',)
	search_fields = ('event_name', 'event_address', 'event_partners')

admin.site.register(Event, EventAdmin)