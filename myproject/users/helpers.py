

from rest_framework.response import Response
from rest_framework import status

class APIResponse:
    @staticmethod
    def format_response(success, message=None, data=None, status_code=None,headers=None):
       
        response_data = {
            'success': success,
            'status': 'success' if success else 'error',
            'message': message if message else ('Success' if success else 'Something went wrong.'),
            'data': data if data else {}
        }
        return Response(response_data, status=status_code if status_code else (status.HTTP_200_OK if success else status.HTTP_400_BAD_REQUEST))
