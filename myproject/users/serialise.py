from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User, UserProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

from .validators import EmailValidator, UniqueEmailValidator, PhoneNumberValidator,StringOnlyValidator

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['address', 'number', 'qualification']
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    firstname = serializers.CharField(validators=[StringOnlyValidator()])
    lastname = serializers.CharField(validators=[StringOnlyValidator()])
    username = serializers.CharField(validators=[StringOnlyValidator()])
    class Meta:
        model = User
        fields = ['id', 'firstname', 'lastname','username','password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        
        # Check if the username already exists
        if User.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already taken."})
        
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user
#custom Authentication    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom response data
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
        }
        return data

# class CourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'

# class StudentSerializer(serializers.ModelSerializer):
#     course_ids = serializers.PrimaryKeyRelatedField(
#         queryset=Course.objects.all(), many=True, write_only=True, source='courses'
#     )
#     courses = CourseSerializer(many=True, read_only=True)
#     full_name = serializers.CharField(validators=[StringOnlyValidator()])

#     class Meta:
#         model = Student
#         fields = ['id', 'full_name', 'email',  'course_ids', 'courses']

#     email = serializers.EmailField(validators=[EmailValidator(), UniqueEmailValidator(queryset=Student.objects.all())])
    

# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Department
#         fields = '__all__'

# class EmployeeSerializer(serializers.ModelSerializer):
#     department_id = serializers.PrimaryKeyRelatedField(
#     queryset=Department.objects.all(), write_only=True, source='department'
#     )
#     department = DepartmentSerializer(read_only=True)
#     full_name = serializers.CharField(validators=[StringOnlyValidator()])
   
    

#     class Meta:
#         model = Employee
#         fields = ['id', 'full_name', 'email','department_id', 'department']

#     email = serializers.EmailField(validators=[EmailValidator(), UniqueEmailValidator(queryset=Employee.objects.all())])




# # class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
# #     @classmethod
# #     def get_token(cls, user):
# #         token = super().get_token(user)
# #         return token

# #     def validate(self, attrs):
# #         data = super().validate(attrs)
# #         # Add custom response data
# #         data['user'] = {
# #             'id': self.user.id,
# #             'username': self.user.username,
# #             'email': self.user.email,
# #             'first_name': self.user.first_name,
# #             'last_name': self.user.last_name,
# #         }
# #         return data

    

  
