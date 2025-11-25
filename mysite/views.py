from django.shortcuts import render

from mysite.services import course_service, dashboard_service, formation_services


def index(request):
    """Render the index page with dashboard statistics and recent activity."""
    stats = dashboard_service.get_dashboard_stats()
    recent_activity = dashboard_service.get_recent_activity()

    context = {**stats, "recent_activity": recent_activity}
    return render(request, "index.html", context)


def projects(request):
    """Render the projects page."""
    context = {}
    return render(request, "projects.html", context)


def formations(request):
    """Render the formations page with all formations."""
    formations_qs = formation_services.get_all_formations()
    context = {
        "formations_qs": formations_qs,
    }
    return render(request, "formations.html", context)


def course(request, pk):
    """Render the course detail page."""
    course_found = course_service.get_course(pk=pk)
    context = {"course": course_found}
    return render(request, "course.html", context)


def courses(request):
    """Render the courses page with all courses."""
    courses_found = course_service.get_courses()
    context = {"courses": courses_found}
    return render(request, "courses.html", context)
