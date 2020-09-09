from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewStudentsList, name='Pass-viewStudentsList'),
    path('viewCheckInProfile/<int:pk>', views.viewCheckInProfile, name='Pass-viewCheckInProfile'),
    path('Pass/<int:pk>', views.Pass, name="Pass-Pass"),
]