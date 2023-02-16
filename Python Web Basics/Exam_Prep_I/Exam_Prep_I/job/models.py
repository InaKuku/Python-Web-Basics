from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.deconstruct import deconstructible

from Exam_Prep_I.job.validators import only_letters_validator, not_below_zero

@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError("Max file size is 5.00 MB")

class Profile(models.Model):

    budget = models.FloatField(
        default=0,
        blank=False,
        validators={
            not_below_zero
        },
    )

    first_name = models.CharField(
        max_length=15,
        blank = False,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        ),
    )

    last_name = models.CharField(
        max_length=15,
        blank = False,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        ),
    )

    profile_image = models.ImageField(
        null = True,
        blank = True,
        upload_to='profiles/',
        validators=(
            MaxFileSizeInMbValidator(5),
        )

    )

class Expense(models.Model):

    title = models.CharField(
        max_length=30,
        blank=False,
    )

    expense_image = models.URLField(
        blank=False,
    )

    description = models.TextField(
        blank = True,
    )

    price = models.FloatField(
        blank = False,
    )

    expenses_creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
