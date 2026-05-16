from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size=6
    page_size_query_param='page_site'
    max_page_size=50