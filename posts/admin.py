from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('meta_title', 'author', 'publication_date', 'is_published', 'get_categories', 'get_image')
	list_display_links = ('meta_title',)
	search_fields = ('meta_title', 'partner_description')
	list_editable = ('is_published',)
	list_per_page = 25

	def get_categories(self, obj):
		return ', '.join([c.category_name for c in obj.post_category.all()])
	get_categories.short_description = 'Categories'

	def get_image(self, obj):
		# show image in object grid
		if obj.featured_image:
			# must check if object exists otherwise throws an error
			return mark_safe('<img src="{thumb}" width="100" />'.format(thumb=obj.featured_image.url,))
		else:
			return 'No image available'
	get_image.allow_tags = True
	get_image.short_description = 'Featured Image'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)