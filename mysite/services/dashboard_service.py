""" "Service functions for dashboard statistics and recent activities."""

from typing import Any, Dict, List

from django.db.models import Sum

from mysite.models import Course, Formation


def get_dashboard_stats() -> Dict[str, Any]:
    """
    Calculates and returns statistics for the dashboard.
    """
    total_courses = Course.objects.filter(is_active=True).count()
    total_formations = Formation.objects.count()

    # Calculate total hours (sum of workload from all courses)
    total_hours_data = Course.objects.filter(is_active=True).aggregate(
        total_hours=Sum("workload")
    )
    total_hours = total_hours_data["total_hours"] or 0

    # Course progress
    courses_completed = Course.objects.filter(
        end_date__isnull=False, is_active=True
    ).count()
    courses_in_progress = Course.objects.filter(
        end_date__isnull=True, is_active=True
    ).count()

    return {
        "total_courses": total_courses,
        "total_formations": total_formations,
        "total_hours": total_hours,
        "courses_completed": courses_completed,
        "courses_in_progress": courses_in_progress,
    }


def get_recent_activity(limit: int = 5) -> List[Dict[str, Any]]:
    """
    Fetches the most recently completed courses.
    Returns a list sorted by end date.
    """
    activities = []

    recent_courses = Course.objects.filter(
        end_date__isnull=False, is_active=True
    ).order_by("-end_date")[:limit]

    for course in recent_courses:
        activities.append(
            {
                "type": "Curso",
                "id": course.pk,
                "description": f"{course.name} ({course.institution.name if course.institution else 'N/A'})",
                "end_date": course.end_date.strftime("%d/%m/%Y"),
                "timestamp": course.end_date,
            }
        )

    return activities
