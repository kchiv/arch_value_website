from django.views.generic.base import TemplateView
from posts.models import Post

class HomePageView(TemplateView):

	template_name = 'template_view/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Post.objects.filter(is_published=True).order_by('-publication_date')[:3]
		return context


class ContactPageView(TemplateView):

	template_name = 'template_view/contact.html'


class OemServicePageView(TemplateView):

	template_name = 'template_view/oem.html'


class DistServicePageView(TemplateView):

	template_name = 'template_view/distributor.html'