"""Tests for the dashboard service."""

import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stevillis_site.settings")
django.setup()

from django.test import TestCase
from django.utils import timezone

from mysite.models import Category, Course, Formation, Institution
from mysite.services import dashboard_service


class DashboardServiceTest(TestCase):
    """Tests for the dashboard service."""

    def setUp(self):
        """Set up test data for dashboard service tests."""
        # Create dummy data
        self.institution = Institution.objects.create(name="Test Inst")
        self.category = Category.objects.create(name="Test Cat")

        # Completed course
        self.course1 = Course.objects.create(
            name="Course 1",
            workload=10,
            start_date=timezone.now().date(),
            end_date=timezone.now().date(),
            institution=self.institution,
        )

        # In-progress course
        self.course2 = Course.objects.create(
            name="Course 2",
            workload=20,
            start_date=timezone.now().date(),
            institution=self.institution,
        )

        # Formation
        self.formation = Formation.objects.create(
            name="Formation 1",
            workload=100,
            start_date=timezone.now().date(),
            end_date=timezone.now().date(),
        )

    def test_get_dashboard_stats(self):
        """Test retrieving dashboard statistics."""
        stats = dashboard_service.get_dashboard_stats()

        self.assertEqual(stats["total_courses"], 2)
        self.assertEqual(stats["total_formations"], 1)
        self.assertEqual(stats["total_hours"], 30)
        self.assertEqual(stats["courses_completed"], 1)
        self.assertEqual(stats["courses_in_progress"], 1)

    def test_get_recent_activity(self):
        """Test retrieving recent activity."""
        activity = dashboard_service.get_recent_activity()
        self.assertTrue(len(activity) > 0)
        self.assertEqual(
            activity[0]["type"], "Formação"
        )  # Most recent activity should be the formation
