from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign up'),
    path('add_spot/', views.add_spot, name='add spot'),
    # path('add_pass/', views.add_pass, name='add password'),

]
