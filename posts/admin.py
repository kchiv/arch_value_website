from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Post, Category, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('get_title', 'get_name', 'publication_date', 'is_published', 'get_categories', 'get_image')
	list_display_links = ('get_title', 'get_image')
	search_fields = ('get_title', 'partner_description')
	list_editable = ('is_published',)
	list_per_page = 25

	def view_on_site(self, obj):
		# adds link to view from django admin object
		url = reverse('post_preview', kwargs={'post_id': obj.pk})
		return url

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

	def get_name(self, obj):
		# user friendly author name display
		return '%s %s' % (obj.author.first_name, obj.author.last_name)

	get_image.allow_tags = True

	# user friendly names in list display
	get_categories.short_description = 'Categories'
	get_image.short_description = 'Featured Image'
	get_title.short_description = 'Title'
	get_name.short_description = 'Author'

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'is_published', 'get_image', 'get_posts')
	list_display_links = ('category_name', 'get_image')
	list_editable = ('is_published',)
	list_per_page = 10

	def get_image(self, obj):
		# show image in object grid
		if obj.category_image:
			# must check if object exists otherwise throws an error
			# mark_safe() used to display html
			return mark_safe('<img src="{thumb}" width="100" />'.format(thumb=obj.category_image.url,))
		else:
			return 'No image available'

	def get_posts(self, obj):
		# gets number of posts in category
		return Post.objects.filter(post_category__pk=obj.pk).count()

	# user friendly names in list display
	get_image.short_description = 'Featured Image'
	get_posts.short_description = '# of posts'

class TagAdmin(admin.ModelAdmin):
	list_display = ('tag_name', 'get_posts')
	list_display_links = ('tag_name',)
	list_per_page = 25

	def get_posts(self, obj):
		# gets number of posts in category
		return Post.objects.filter(post_tag__pk=obj.pk).count()

	# user friendly names in list display
	get_posts.short_description = '# of posts'

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)