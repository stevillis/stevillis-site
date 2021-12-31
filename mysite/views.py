from django.shortcuts import render

from mysite.services import formation_services


def index(request):
    context = {}
    return render(request, "index.html", context)


def projects(request):
    context = {}
    return render(request, "projects.html", context)


def formations(request):
    formations_qs = formation_services.get_all_formations()
    context = {
        'formations_qs': formations_qs,
    }
    return render(request, "formations.html", context)
