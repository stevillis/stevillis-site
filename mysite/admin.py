from django.contrib import admin

from mysite.models import Category, Institution, Formation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ['name']


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ['name']


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    fields = ['name', 'workload', 'curriculum_map', 'start_date', 'end_date']
    list_display = ('name', 'workload', 'start_date', 'end_date', 'created_at', 'updated_at',)
    search_fields = ['name']
