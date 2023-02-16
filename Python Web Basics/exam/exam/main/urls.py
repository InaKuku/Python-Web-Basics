from django.urls import path
from exam.main.views import show_home, create_album, edit_album, delete_album, show_profile, \
    delete_profile, create_profile, details_album

urlpatterns = [
    path('', show_home, name='home'),

    path('album/add/', create_album, name='create album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('album/details/<int:pk>/', details_album, name='details album'),

    path('profile/details/', show_profile, name='show profile'),
    path('create_profile/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]

