from django.urls import path

from .views import formations, index, projects

urlpatterns = [
    path("", index, name="index"),
    path("projects/", projects, name="projects"),
    path("formations/", formations, name="formations"),
]
