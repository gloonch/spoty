from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign up'),
    path('sign_in/', views.sign_in, name='sign in'),
    # spot CRUD
    path('add_spot/', views.add_spot, name='add spot'),
    path('delete_spot/', views.delete_spot, name='delete spot'),
]
