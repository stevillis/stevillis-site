from typing import Tuple

from django.db.models import QuerySet
from django.http import Http404
from django.utils.translation import gettext as _

from mysite.models import Course


def get_course(pk: int) -> Tuple[Course, Http404]:
    try:
        return Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        raise Http404(_('Course not found!'))


def get_courses() -> QuerySet:
    return Course.objects.all().order_by('-end_date', '-start_date')
