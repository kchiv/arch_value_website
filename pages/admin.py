from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	list_display = ('meta_title', 'is_published', 'show_cta')
	list_display_links = ('meta_title',)
	list_editable = ('is_published', 'show_cta')
	list_per_page = 25

admin.site.register(Page, PageAdmin)
