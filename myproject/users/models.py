from django.db import models

# one-to-one relationship between user and userprofile
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255, null=True, blank=False)
    number = models.CharField(max_length=255, null=True)
    qualification = models.CharField(max_length=255, null=True)

# class Course(models.Model):
#     course_name = models.CharField(max_length=255,null=True)
#     course_desc=models.CharField(max_length=255,null=True)  
    
#     def __str__(self):
#       return f"{self.course_name}{self. course_desc}"
  
# class Student(models.Model):
   
#     full_name = models.CharField(max_length=100,null=True)
#     email = models.CharField(max_length=100,null=True)
#     courses = models.ManyToManyField(Course, related_name='students')

#     def __str__(self):
#         return f"{self.full_name}"
    
# #one to many between dept and emp
    
# class Department(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Employee(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

#     def __str__(self):
#         return self.full_name
    

  
    

    
