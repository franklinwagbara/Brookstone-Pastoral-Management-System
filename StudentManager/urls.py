from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManageStudents, name='StudentManager-ManageStudents'),
    path('viewUpdateStudentRecord/<int:pk>', views.viewUpdateStudentRecord, name="StudentManager-viewUpdateStudentRecord"),
    path('viewDeleteStudentRecord/<int:pk>', views.viewDeleteStudentRecord, name="StudentManager-viewDeleteStudentRecord"),
    path('viewAddStudent', views.viewAddStudent, name="StudentManager-viewAddStudent"),
    path('allowStudent/<int:pk>', views.allowStudent, name="StudentManager-allowStudent"),
    path('viewStudentProfile/<int:pk>', views.viewStudentProfile, name="StudentManager-viewStudentProfile"),
]