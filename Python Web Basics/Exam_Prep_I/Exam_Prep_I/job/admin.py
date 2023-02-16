from django.contrib import admin

from Exam_Prep_I.job.models import Profile


@admin.register(Profile)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('id', 'first_name', 'last_name', 'budget')
