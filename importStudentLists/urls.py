from django.urls import path
from . import views

urlpatterns = [
    path('', views.importStudentLists, name="importStudentLists-importStudentLists"),
    path('importTemplate', views.importTemplate, name="importStudentLists-importTemplate"),
    path('test', views.test, name="importStudentLists-test"),
]