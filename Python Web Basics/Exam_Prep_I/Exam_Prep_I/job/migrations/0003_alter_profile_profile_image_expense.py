# Generated by Django 4.0.2 on 2022-02-20 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('expense_image', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('expenses_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.profile')),
            ],
        ),
    ]
