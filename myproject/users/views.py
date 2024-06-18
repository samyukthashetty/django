from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import user, userprofile, Student, Course, Employee, Department
from .serialise import UserSerializer, StudentSerializer, CourseSerializer, EmployeeSerializer, DepartmentSerializer
import logging
from rest_framework import serializers
from .helpers import APIResponse


logger = logging.getLogger(__name__)

# class ApiOverview(APIView):
#     def get(self, request):
#         api_urls = {
#             'Create User': '/create/',
#             'View All Users': '/all/',
#             'Create Student': '/createstudent/',
#             'view all students':'/getall/',
#             'create Employee':'/CreateEmp/',
#             'view all employees':'/getemp/',
#         }
#         return Response(api_urls)


#User create 

class UserCreateView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data) #validating serializor
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)#save serializer
            headers = self.get_success_headers(serializer.data)
            return APIResponse.format_response(True, 'User created successfully', serializer.data, status.HTTP_201_CREATED, headers)
                
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error in UserCreateView: {e}")
            return Response(False,'Internal Server error',status.HTTP_500_INTERNAL_SERVER_ERROR)
 #display users                
class UserListView(generics.ListAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()#get the list of items 
            serializer = self.get_serializer(queryset, many=True)
            return APIResponse.format_response(True,'Users List', serializer.data, status.HTTP_200_OK)
       
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in UserListView: {e}")
            return APIResponse.format_response(False,'Internal Server error',status.HTTP_500_INTERNAL_SERVER_ERROR)
#create course
class CourseListCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return APIResponse.format_response(True,'Course has been crested',response.data,status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in CourseListCreateView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#View courses
class CourseDetailView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return APIResponse.format_response(True,'CourseDetails',serializer.data, status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in CourseDetailView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#create student using particular course ID
class StudentListCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return APIResponse.format_response(True,'Student has been created',response.data,status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in StudentListCreateView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#get all students
class StudentDetailView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return APIResponse.format_response(True,'ViewStudents',serializer.data, status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in StudentDetailView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#Department creation 
class DepartmentListCreateView(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return APIResponse.format_response(True,'dept has been created',response.data,status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in DepartmentListCreateView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#details of dept
class DepartmentDetailView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return APIResponse.format_response(True,'deptdetails',serializer.data, status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in DepartmentDetailView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#employee creation
class EmployeeListCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return APIResponse.format_response(True,'Employee created',response.data,status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in EmployeeListCreateView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)
#employee details
class EmployeeDetailView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return APIResponse.format_response(True,'employee Details',serializer.data, status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return APIResponse.format_response(False, str(e.detail), status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(f"Error in EmployeeDetailView: {e}")
            return APIResponse.format_response(False,'Internal Server error', status.HTTP_500_INTERNAL_SERVER_ERROR)