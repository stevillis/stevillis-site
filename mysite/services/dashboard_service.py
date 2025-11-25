from typing import Any, Dict, List

from django.db.models import Sum

from mysite.models import Course, Formation


def get_dashboard_stats() -> Dict[str, Any]:
    """
    Calculates and returns statistics for the dashboard.
    """
    total_courses = Course.objects.count()
    total_formations = Formation.objects.count()

    # Calculate total hours (sum of workload from all courses)
    total_hours_data = Course.objects.aggregate(total_hours=Sum("workload"))
    total_hours = total_hours_data["total_hours"] or 0

    # Course progress
    courses_completed = Course.objects.filter(end_date__isnull=False).count()
    courses_in_progress = Course.objects.filter(end_date__isnull=True).count()

    return {
        "total_courses": total_courses,
        "total_formations": total_formations,
        "total_hours": total_hours,
        "courses_completed": courses_completed,
        "courses_in_progress": courses_in_progress,
    }


def get_recent_activity(limit: int = 5) -> List[Dict[str, Any]]:
    """
    Simulates recent activity by fetching the most recently updated courses
    and formations.
    Returns a unified list sorted by date.
    """
    activities = []

    recent_courses = Course.objects.order_by("-updated_at")[:limit]
    for course in recent_courses:
        activities.append(
            {
                "type": "Curso",
                "id": course.pk,
                "description": f"{course.name} ({course.institution.name if course.institution else 'N/A'})",
                "date": course.updated_at.strftime("%d/%m/%Y"),
                "timestamp": course.updated_at,
            }
        )

    recent_formations = Formation.objects.order_by("-updated_at")[:limit]
    for formation in recent_formations:
        activities.append(
            {
                "type": "Formação",
                "id": formation.pk,
                "description": formation.name,
                "date": formation.updated_at.strftime("%d/%m/%Y"),
                "timestamp": formation.updated_at,
            }
        )

    activities.sort(key=lambda x: x["timestamp"], reverse=True)
    return activities[:limit]
