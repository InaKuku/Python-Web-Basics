from django.urls import path
from Exam_Prep_IV.main.views import show_home, details_recipe, edit_recipe, create_recipe, delete_recipe

urlpatterns = [
    path('', show_home, name='home'),

    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe'),

]
