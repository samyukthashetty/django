# # import time
# # import logging

# logger = logging.getLogger(__name__)

# class RequestTimingMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#          start_time = time.time()
        
#          response = self.get_response(request)
        
#          duration = time.time() - start_time
        #  logger.info("Request to {request.path} took {duration:.2f} seconds")
        
#          return response

#Creating Temporary CustomMiddleware Configuration
# class TemporaryMiddleware:
    
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
      
#         print('TemporaryMiddleware: Before processing request')
    

#         response = self.get_response(request)
       

#         print('TemporaryMiddleware: After processing request')
        
#         return response

# from django.utils.deprecation import MiddlewareMixin
# from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.exceptions import ValidationError, APIException

# class CustomMiddleware(MiddlewareMixin):
    
#     # def process_view(self, request, view_func, view_args, view_kwargs):
#     #     if request.method == 'POST' :
#     #         return JsonResponse({
#     #             'success': False,
#     #             'code': 403,
#     #             'error':'Authentication required for creating a user.'
#     #         }, status=status.HTTP_403_FORBIDDEN)
#     #     return None

#     def process_exception(self, request, exception):
         
#         if isinstance(exception, ValueError):
           
#             return JsonResponse({
#                 'error': str(exception),
#                 'code': 400,
#                 'success': False
#             }, status=status.HTTP_400_BAD_REQUEST)
        
#         return None
    
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError 




from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import serializers
import logging
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger(__name__)

class CustomExceptionMiddleware(MiddlewareMixin):
  

    
 def process_exception(self, request, exception):
        

        if isinstance(exception, ValidationError):

            return JsonResponse({'success': False, 'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)
           

        elif isinstance(exception, ValueError):
           
            return JsonResponse({'success': False, 'error': str(exception)}, status=status.HTTP_400_BAD_REQUEST)

        # elif isinstance(exception, Exception):
            
        #     return JsonResponse({'success': False, 'error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        