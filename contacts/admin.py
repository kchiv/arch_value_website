from django.contrib import admin

from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'user_type', 'email', 'company_name', 'contact_date')
	list_display_links = ('name', 'email')
	search_fields = ('name', 'email', 'company_name')
	list_per_page = 25

admin.site.register(Contact, ContactAdmin)