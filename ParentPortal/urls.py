from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='ParentPortal-home'),
    path('parentForm/<int:pk>', views.parentForm, name="ParentPortal-parentForm"),
]