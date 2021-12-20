from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from mysite.models import Category, Course, Formation, Institution


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ['name']
    ordering = ['name']


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ['name']
    ordering = ['name']


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    fields = ['name', 'workload', 'description', 'start_date', 'end_date']
    list_display = ('name', 'workload', 'start_date', 'end_date', 'created_at', 'updated_at',)
    search_fields = ['name']
    ordering = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'workload', 'curriculum_map', 'start_date', 'end_date', 'institution', 'categories', 'formation']
    list_display = ('name', 'workload', 'start_date', 'end_date', 'created_at', 'updated_at', 'institution',)
    list_filter = [
        ('institution', custom_titled_filter(_('Institution'))),
        ('formation', custom_titled_filter(_('Formation'))),
        ('categories', custom_titled_filter(_('Category')))
    ]
    search_fields = ['name']
    ordering = ['-end_date']
