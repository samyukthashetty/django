from rest_framework import serializers
from .models import user, userprofile, Student, Course, Employee, Department
from .validators import EmailValidator, UniqueEmailValidator, PhoneNumberValidator,StringOnlyValidator

class UserProfileSerializer(serializers.ModelSerializer):
    number = serializers.CharField(validators=[PhoneNumberValidator()])
    Address = serializers.CharField(validators=[StringOnlyValidator()])
    qualification = serializers.CharField(validators=[StringOnlyValidator()])
    class Meta:
        model = userprofile
        fields = ['Address', 'number', 'qualification']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    firstname = serializers.CharField(validators=[StringOnlyValidator()])
    lastname = serializers.CharField(validators=[StringOnlyValidator()])
   
    class Meta:
        model = user
        fields = ['id', 'firstname', 'lastname', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        instance = user.objects.create(**validated_data)
        userprofile.objects.create(user=instance, **profile_data)
        return instance
   

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    course_ids = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(), many=True, write_only=True, source='courses'
    )
    courses = CourseSerializer(many=True, read_only=True)
    full_name = serializers.CharField(validators=[StringOnlyValidator()])

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'email',  'course_ids', 'courses']

    email = serializers.EmailField(validators=[EmailValidator(), UniqueEmailValidator(queryset=Student.objects.all())])
    

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    department_id = serializers.PrimaryKeyRelatedField(
    queryset=Department.objects.all(), write_only=True, source='department'
    )
    department = DepartmentSerializer(read_only=True)
    full_name = serializers.CharField(validators=[StringOnlyValidator()])
   
    

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'email','department_id', 'department']

    email = serializers.EmailField(validators=[EmailValidator(), UniqueEmailValidator(queryset=Employee.objects.all())])
    

  
