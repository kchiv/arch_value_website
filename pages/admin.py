from django.contrib import admin
from django.urls import reverse
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('meta_title', 'is_published', 'show_cta')
	list_display_links = ('meta_title',)
	list_editable = ('is_published', 'show_cta')
	list_per_page = 25

	def view_on_site(self, obj):
		# adds link to view from django admin object
		url = reverse('page_preview', kwargs={'page_id': obj.pk})
		return url

admin.site.register(Page, PageAdmin)
