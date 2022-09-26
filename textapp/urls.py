from django.urls import path
from textapp import views

urlpatterns = [
    path("", views.index, name="index")
]