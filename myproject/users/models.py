from django.db import models
# one-to-one relationship between user and userprofile
class user(models.Model):
     firstname = models.CharField(max_length=255,null=True)
     lastname = models.CharField(max_length=255,null=True)
     
     def __str__(self):
      return f"{self.firstname}{self.lastname}"

     
class userprofile(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, related_name='profile')
    Address = models.CharField(max_length=255,null=True,blank=False)
    number = models.CharField(max_length=255,null=True)
    qualification = models.CharField(max_length=255,null=True)
    
# Many-to-Many ralationship  between Course and Student
    
class Course(models.Model):
    course_name = models.CharField(max_length=255,null=True)
    course_desc=models.CharField(max_length=255,null=True)  
    
    def __str__(self):
      return f"{self.course_name}{self. course_desc}"
  
class Student(models.Model):
   
    full_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.full_name}"
    
#one to many between dept and emp
    
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.full_name
    

  
    

    
