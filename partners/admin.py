from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Partner

# Register your models here.

class PartnerAdmin(admin.ModelAdmin):
	list_display = ('partner_name', 'get_image')
	list_display_links = ('partner_name', 'get_image')
	search_fields = ('partner_name', 'partner_description')
	list_per_page = 25

	def get_image(self, obj):
		# show image in object grid
		if obj.partner_logo:
			# must check if object exists otherwise throws an error
			return mark_safe('<img src="{thumb}" width="100" />'.format(thumb=obj.partner_logo.url,))
		else:
			return 'No image available'
	get_image.allow_tags = True
	get_image.short_description = 'Partner logo'

admin.site.register(Partner, PartnerAdmin)
