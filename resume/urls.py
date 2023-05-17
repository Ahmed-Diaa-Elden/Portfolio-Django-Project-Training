from django.urls import path
from . import views

urlpatterns = [
  path('resume/', views.resume , name="resume"),
  path('contactFormValidation/', views.contactFormValidation, name ='contactFormValidation'),
  path('contactFormValidationList', views.contactFormValidationList, name ='contactFormValidationList'),
]