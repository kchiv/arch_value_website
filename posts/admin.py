from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('get_title', 'author', 'publication_date', 'is_published', 'get_categories', 'get_image')
	list_display_links = ('get_title',)
	search_fields = ('get_title', 'partner_description')
	list_editable = ('is_published',)
	list_per_page = 25

	def get_categories(self, obj):
		# loop through and dsiplay category names
		return ', '.join([c.category_name for c in obj.post_category.all()])

	def get_image(self, obj):
		# show image in object grid
		if obj.featured_image:
			# must check if object exists otherwise throws an error
			# mark_safe() used to display html
			return mark_safe('<img src="{thumb}" width="100" />'.format(thumb=obj.featured_image.url,))
		else:
			return 'No image available'

	def get_title(self, obj):
		# method foundation for user friendly title name in list display
		if obj.meta_title:
			return obj.meta_title
		else:
			return 'No title available'

	get_image.allow_tags = True

	# user friendly names in list display
	get_categories.short_description = 'Categories'
	get_image.short_description = 'Featured Image'
	get_title.short_description = 'Title'

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)