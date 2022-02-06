from django.urls import path

from .views import course, formations, index, projects

urlpatterns = [
    path("", index, name="index"),
    path("projects/", projects, name="projects"),
    path("formations/", formations, name="formations"),
    path("course/<int:pk>", course, name="course"),
]
