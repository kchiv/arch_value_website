from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('meta_title', 'author', 'publication_date', 'is_published', 'get_categories')
	list_display_links = ('meta_title',)
	search_fields = ('meta_title', 'partner_description')
	list_editable = ('is_published',)
	list_per_page = 25

	def get_categories(self, obj):
		return ', '.join([c.category_name for c in obj.post_category.all()])
	get_categories.short_description = 'Categories'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)