# Generated by Django 3.2.9 on 2021-12-20 02:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_alter_formation_workload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mysite.institution'),
        ),
    ]
