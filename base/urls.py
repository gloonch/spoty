from django.urls import path
from . import views

urlpatterns = [
    path('is_email_registered/', views.is_email_registered, name="is_email_registered"),
    path('generate_token/', views.generate_token, name="generate_token"),
]
