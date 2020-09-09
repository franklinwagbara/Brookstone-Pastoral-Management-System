from django.urls import path
from . import views

urlpatterns = [
    path('', views.createSeason, name="Manager-createSeason"),
    path('changeCurrentSeason', views.changeCurrentSeason, name="Manager-changeCurrentSeason"),
    path('viewSettings', views.viewSettings, name="Manager-viewSettings"),
]