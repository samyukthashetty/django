from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError as DRFValidationError

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, DRFValidationError):
        # Re-raise the exception to be caught by middleware
        raise exc

    return response
