from django.urls import path
from Exam_Prep_I.job.views import show_home, create_expense, edit_expense, delete_expense, show_profile, edit_profile, \
    delete_profile, create_profile

urlpatterns = [
    path('', show_home, name='home'),

    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),

    path('create-profile/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
