from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 10

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)
        self.offset = self.get_offset(request)
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response({
            'success': True,
            'code': 200,
            'data': {
                'results': data,
                'count': self.count,
            }
        })

    def get_offset(self, request):
        offset = int(request.data.get('offset', 0))
        return offset

    def get_limit(self, request):
        limit = int(request.data.get('limit', self.default_limit))
        return limit
