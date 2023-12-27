from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("nazar", views.nazar, name="nazar"),
    path("<str:name>", views.greet, name="greet")
]