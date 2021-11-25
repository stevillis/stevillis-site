from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context)


def projects(request):
    context = {}
    return render(request, "projects.html", context)
