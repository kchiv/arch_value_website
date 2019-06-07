from django.conf import settings
from rest_framework import pagination


class PartnersResultsPagination(pagination.PageNumberPagination):
	page_size = 9
	page_size_query_param = 'page_size'
	max_page_size = 1000

	def get_paginated_response(self, data):
		response = super(PartnersResultsPagination, self).get_paginated_response(data)
		response.data['total_pages'] = self.page.paginator.num_pages
		if self.page.has_previous():
			response.data['prev_page_num'] = self.page.previous_page_number()
		else:
			response.data['prev_page_num'] = None

		if self.page.has_next():
			response.data['nex_page_num'] = self.page.next_page_number()
		else:
			response.data['nex_page_num'] = None
		return response