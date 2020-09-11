from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewStudentsList, name='Pass-viewStudentsList'),
    path('viewCheckInProfile/<int:pk>', views.viewCheckInProfile, name='Pass-viewCheckInProfile'),
    path('viewCheckInProfileAdmin/<int:pk>', views.viewCheckInProfileAdmin, name='Pass-viewCheckInProfile'),
    path('Pass/<int:pk>', views.Pass, name="Pass-Pass"),
    path('Pass_Admin/', views.viewStudentsListAdmin, name="Pass-viewStudentsListAdmin"),
    path('Pass_Admin/<int:pk>', views.PassAdmin, name="Pass-PassAdmin"),
]