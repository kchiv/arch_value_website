from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'is_published', 'event_start', 'event_end', 'event_country', 'event_city', 'event_state', 'get_partners')
	list_display_links = ('event_name',)
	search_fields = ('event_name', 'event_country', 'event_city', 'event_state', 'event_partners')
	list_editable = ('is_published',)
	list_per_page = 25

	def get_partners(self, obj):
		return ', '.join([p.partner_name for p in obj.event_partners.all()])
	get_partners.short_description = 'Partners'

admin.site.register(Event, EventAdmin)