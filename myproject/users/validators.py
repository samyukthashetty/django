from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import user
import re
class EmailValidator:
    def __call__(self, value):
        try:
            validate_email(value)
        except ValidationError:
             raise serializers.ValidationError(
                 'Invalid email format.'
            )

class UniqueEmailValidator:
    def __init__(self, queryset=None):
        self.queryset = queryset

    def __call__(self, value):
        if self.queryset.filter(email=value).exists():
             raise serializers.ValidationError(
               'Email is already in use.'
            )

class StringOnlyValidator:
    def __call__(self, value):
       
        if not value.isalpha():
            raise serializers.ValidationError("This field must contain only alphabetic characters.")

class PhoneNumberValidator:
    def __call__(self, value):
        phone_pattern = re.compile(r'^\+?1?\d{10}$')  
        if not phone_pattern.match(value):
            raise serializers.ValidationError('Invalid phone number format.')
                 

