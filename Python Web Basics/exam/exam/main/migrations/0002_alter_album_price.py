# Generated by Django 4.0.2 on 2022-02-27 09:21

from django.db import migrations, models
import exam.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(verbose_name=exam.main.validators.check_float_zero),
        ),
    ]
