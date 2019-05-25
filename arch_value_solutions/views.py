from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

	template_name = 'template_view/index.html'


class ContactPageView(TemplateView):

	template_name = 'template_view/contact.html'


class OemServicePageView(TemplateView):

	template_name = 'template_view/oem.html'


class DistServicePageView(TemplateView):

	template_name = 'template_view/distributor.html'