from django.core.exceptions import ValidationError


def letters_numbers_underscore_validator(value):
    for ch in value:
        if not ch.isalpha() and not ch.isdigit() and not ch == '_':
           raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')

def check_float_zero(value):
    if not value >= 0.0:
        raise ValidationError('Ensure this value is over 0.0')