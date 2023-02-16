from django.urls import path
from pattern.main.views import show_home, create_note, edit_note, delete_note, show_profile, \
    delete_profile, create_profile, details_note

urlpatterns = [
    path('', show_home, name='home'),

    path('add/', create_note, name='create note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),

    path('profile/', show_profile, name='show profile'),
    path('create_profile/', create_profile, name='create profile'),
    path('delete_profile/', delete_profile, name='delete profile'),
]

