from django.shortcuts import render

from mysite.services import course_service, formation_services


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


def course(request, pk):
    course_found = course_service.get_course(pk=pk)
    context = {
        'course': course_found
    }
    return render(request, 'course.html', context)


def courses(request):
    courses_found = course_service.get_courses()
    context = {
        'courses': courses_found
    }
    return render(request, 'courses.html', context)
