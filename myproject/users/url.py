from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='CreateAPIView'),
    path('all/', views.UserListView.as_view(), name='UserListView'),
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('getall/', views.CourseDetailView.as_view(), name='course-detail'),
    path('students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('getstudents/', views.StudentDetailView.as_view(), name='student-detail'),
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('getdept/',views. DepartmentDetailView.as_view(), name='department-detail'),
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('getemp/',views. EmployeeDetailView.as_view(), name='employee-detail'),
    
]
