from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Dashboard-home'),
    path('RegisterStaff/', views.sendStaffMail, name="Dashboard-SendStaffMail"),
]