from django.contrib import admin

from mysite.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    search_fields = ['name']
