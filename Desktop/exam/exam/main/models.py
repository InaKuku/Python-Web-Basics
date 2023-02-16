from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam.main.validators import letters_numbers_underscore_validator, check_float_zero


class Profile(models.Model):

    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(2),
            letters_numbers_underscore_validator,
        )
    )


    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(0),
        )
    )




class Album(models.Model):

    album_name = models.CharField(
        max_length=30,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=(
            ('Pop Music', 'Pop Music',),
            ('Jazz Music', 'Jazz Music',),
            ('R&B Music', 'R&B Music',),
            ('Rock Music', 'Rock Music',),
            ('Country Music', 'Country Music',),
            ('Dance Music', 'Dance Music',),
            ('Hip Hop Music', 'Hip Hop Music',),
            ('Other', 'Other',),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_URL = models.URLField()

    price = models.FloatField(
        validators=(
            # MinValueValidator(0.0),
            check_float_zero,
        )
    )
