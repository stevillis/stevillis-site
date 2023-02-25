# Generated by Django 3.2.6 on 2022-02-24 17:23
import re

from django.db import migrations, models


def convert_workload(workload):
    return float(re.sub(r'\s[a-zA-Z]+', '', workload))


def convert_formation_workload(apps):
    Formation = apps.get_model('mysite', 'Formation')
    formations = Formation.objects.all()
    for formation in formations:
        formation.workload = convert_workload(formation.workload)
        formation.save()


def convert_course_workload(apps):
    Course = apps.get_model('mysite', 'Course')
    courses = Course.objects.all()
    for course in courses:
        course.workload = convert_workload(course.workload)
        course.save()


def convert_workloads(apps, schema_editor):
    convert_formation_workload(apps)
    convert_course_workload(apps)


class Migration(migrations.Migration):
    dependencies = [
        ('mysite', '0017_auto_20220205_1030'),
    ]

    operations = [
        migrations.RunPython(convert_workloads),

        migrations.AlterField(
            model_name='course',
            name='workload',
            field=models.FloatField(verbose_name='Workload'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='workload',
            field=models.FloatField(blank=True, null=True, verbose_name='Workload'),
        ),
    ]