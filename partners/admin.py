from django.contrib import admin

from .models import Partner

# Register your models here.

class PartnerAdmin(admin.ModelAdmin):
	list_display = ('partner_name',)
	list_display_links = ('partner_name',)
	search_fields = ('partner_name', 'partner_description')
	list_per_page = 25

admin.site.register(Partner, PartnerAdmin)
