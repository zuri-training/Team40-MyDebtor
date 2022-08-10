from rest_framework.pagination import PageNumberPagination


class StudentPaginator (PageNumberPagination):
    page_size = 10