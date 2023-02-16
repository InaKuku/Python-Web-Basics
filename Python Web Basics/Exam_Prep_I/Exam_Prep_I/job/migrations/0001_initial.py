# Generated by Django 4.0.2 on 2022-02-20 16:45

import Exam_Prep_I.job.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), Exam_Prep_I.job.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), Exam_Prep_I.job.validators.only_letters_validator])),
                ('budget', models.FloatField(default=0, validators=[Exam_Prep_I.job.validators.not_below_zero])),
                ('profile_image', models.ImageField(blank=True, default='user.png', null=True, upload_to='')),
            ],
        ),
    ]
