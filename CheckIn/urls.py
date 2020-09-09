from django.urls import path
from . import views

urlpatterns = [
    path('', views.verifyPass, name='CheckIn-verifyPass'),
    path('viewCheckInProfile/<int:pk>', views.viewCheckInProfile, name='CheckIn-viewCheckInProfile'),
    path('CheckIn/<int:pk>', views.Check_In, name="CheckIn-CheckIn"),
    path('DenyEntry/<int:pk>', views.denyEntry, name="CheckIn-DenyEntry"),
]