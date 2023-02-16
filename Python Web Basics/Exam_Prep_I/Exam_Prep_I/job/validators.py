from django.core.exceptions import ValidationError


# def only_letters_validator(value):
#     for ch in value:
#         if not ch.isalpha():
#            raise ValidationError('Ensure this value contains only letters.')

def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Ensure this value contains only letters.')


def not_below_zero(value):
    if value < 0:
        raise ValidationError('The budget should not be below 0')

