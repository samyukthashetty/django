from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.validators import validate_email
from .models import User
import re
class EmailValidator:
    def __call__(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError('Invalid email format.')

class UniqueEmailValidator:
    def __init__(self, queryset=None):
        self.queryset = queryset

    def __call__(self, value):
        if self.queryset.filter(email=value).exists():
            raise serializers.ValidationError('Email is already in use.')

class StringOnlyValidator:
    def __call__(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("This field must contain only alphabetic characters.")

class PhoneNumberValidator:
    def __call__(self, value):
        phone_pattern = re.compile(r'^\+?1?\d{10}$')  
        if not phone_pattern.match(value):
            raise serializers.ValidationError('Invalid phone number format.')
class PaginationValidator:
    @staticmethod
    def validate_offset(offset):
        
        try:
            offset = int(offset)
            if offset < 0:
                raise ValueError('Offset must be a non-negative integer')
            return offset
        except (TypeError, ValueError):
            raise ValueError('Offset must be an integer')

    @staticmethod
    def validate_limit(limit, default_limit=1, max_limit=10):
       
        try:
            limit = int(limit)
            if limit <= 0:
                raise ValueError('Limit must be greater than 0')
            if limit > max_limit:
                limit = max_limit
            return limit
        except (TypeError, ValueError):
            raise ValueError('Limit must be an integer and greater than 0')
