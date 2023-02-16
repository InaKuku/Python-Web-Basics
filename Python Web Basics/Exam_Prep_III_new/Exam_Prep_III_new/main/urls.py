from django.urls import path
from Exam_Prep_III_new.main.views import show_home, create_book, edit_book, delete_book, show_profile, edit_profile, \
    delete_profile, create_profile, details_book

urlpatterns = [
    path('', show_home, name='home'),

    path('add/', create_book, name='create book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', details_book, name='details book'),

    path('create-profile/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]