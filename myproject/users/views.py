# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import user, userprofile, Student, Course, Employee, Department
# from .serialise import UserSerializer, StudentSerializer, CourseSerializer, EmployeeSerializer, DepartmentSerializer
 


# logger = logging.getLogger(__name__)

# # class ApiOverview(APIView):
# #     def get(self, request):
# #         api_urls = {
# #             'Create User': '/create/',
# #             'View All Users': '/all/',
# #             'Create Student': '/createstudent/',
# #             'view all students':'/getall/',
# #             'create Employee':'/CreateEmp/',
# #             'view all employees':'/getemp/',
# #         }
# #         return Response(api_urls)


# #User create 

# class UserCreateView(generics.CreateAPIView):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(data=request.data) #validating serializor
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)#save serializer
#             headers = self.get_success_headers(serializer.data)
#             return APIResponse.format_response(True, 'User created successfully', serializer.data, status.HTTP_201_CREATED, headers)
                
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             logger.error(f"Error in UserCreateView: {e}")
#             return Response(False,'Internal Server error',status.HTTP_500_INTERNAL_SERVER_ERROR)
#  #display users                
# class UserListView(generics.ListAPIView):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()#get the list of items 
#             serializer = self.get_serializer(queryset, many=True)
#             return APIResponse.format_response(True,'Users List', serializer.data, status.HTTP_200_OK)
       
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in UserListView: {e}")
#             return APIResponse.format_response(False,'Internal Server error',status.HTTP_500_INTERNAL_SERVER_ERROR)
# #create course
# class CourseListCreateView(generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'Course has been crested',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in CourseListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #View courses
# class CourseDetailView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)
#             return APIResponse.format_response(True,'CourseDetails',serializer.data, status.HTTP_200_OK)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in CourseDetailView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #create student using particular course ID
# class StudentListCreateView(generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'Student has been created',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in StudentListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #get all students
# class StudentDetailView(generics.ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)
#             return APIResponse.format_response(True,'ViewStudents',serializer.data, status.HTTP_200_OK)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in StudentDetailView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #Department creation 
# class DepartmentListCreateView(generics.CreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'dept has been created',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in DepartmentListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #details of dept
# class DepartmentDetailView(generics.ListAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)
#             return APIResponse.format_response(True,'deptdetails',serializer.data, status.HTTP_200_OK)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in DepartmentDetailView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #employee creation
# class EmployeeListCreateView(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def create(self, request, *args, **kwargs):
#         try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'Employee created',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in EmployeeListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
# #employee details
# class EmployeeDetailView(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)
#             return APIResponse.format_response(True,'employee Details',serializer.data, status.HTTP_200_OK)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in EmployeeDetailView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)



    
#USING MIXINS

from urllib import response
from rest_framework import mixins, generics, status
from rest_framework.exceptions import ValidationError
from .models import User
from .serialise import UserSerializer,UserProfileSerializer,CustomTokenObtainPairSerializer


from .pagination import CustomLimitOffsetPagination


from rest_framework.response import Response
from .validators import PaginationValidator
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
#authentication imports
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from django.db import IntegrityError








class UserCreateListView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomLimitOffsetPagination
    #Authentication 
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
  
    
    def get(self, request, *args, **kwargs):
        offset = PaginationValidator.validate_offset(request.query_params.get('offset', 0))
        limit = PaginationValidator.validate_limit(request.query_params.get('limit', CustomLimitOffsetPagination.default_limit))

        queryset = self.get_queryset()
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request, view=self)

        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
   

        # except serializers.ValidationError as e:
        #     # Handle validation errors raised by serializers
        #     return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # except Exception as e:
        #     # Handle other exceptions
        #     return Response({'success': False, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # except serializers.ValidationError as e:
        #     raise e
        
        # except Exception as e:
        #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# # #create course
# class CourseListCreateView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

   
#     def post(self, request, *args, **kwargs):
#         try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'Course has been crested',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in CourseListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
       
            
        
  
    
#  #create student using particular course ID
# class StudentListCreateView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         try:
#          response = super().create(request, *args, **kwargs)
#          return APIResponse.format_response(True,'Student has been created',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in StudentListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
#  #Department creation 
# class DepartmentListCreateView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'dept has been created',response.data,status.HTTP_201_CREATED)
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             logger.error(f"Error in DepartmentListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        

#  #employee creation
# class EmployeeListCreateView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#          try:
#             response = super().create(request, *args, **kwargs)
#             return APIResponse.format_response(True,'Employee created',response.data,status.HTTP_201_CREATED)
#          except serializers.ValidationError as e:
#             return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
#          except Exception as e:
#             logger.error(f"Error in EmployeeListCreateView: {e}")
#             return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
        
  #USING CONCRETE CLASSES
# from rest_framework import mixins, generics,status
# from .models import user,Course,Student,Department,Employee
# from .serialise import UserSerializer,CourseSerializer,StudentSerializer,DepartmentSerializer,EmployeeSerializer
# from .pagination import SetPagination
# import logging
# from rest_framework import serializers
# from .helpers import APIResponse

# logger = logging.getLogger(__name__)

# class UserCreateListView(generics.ListCreateAPIView):
#      queryset = user.objects.all()
#      serializer_class = UserSerializer
#      def create(self, request, *args, **kwargs):
         
#         try:
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             headers = self.get_success_headers(serializer.data)
#             return APIResponse.format_response(
#                 success=True,
#                 message="User created successfully.",
#                 data=serializer.data,
#                 status_code=status.HTTP_201_CREATED,
#                 headers=headers
#             )
#         except serializers.ValidationError as e:
#             return APIResponse.format_response(
#                 success=False,
#                 message=str(e.detail),
#                 status_code=status.HTTP_400_BAD_REQUEST
#             )
#         except Exception as e:
#             return APIResponse.format_response(
#                 success=False,
#                 message=str(e),
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
      

    

    

    