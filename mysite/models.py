from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    id_category = models.AutoField(_('Category ID'), primary_key=True)
    name = models.CharField(_('Name'), max_length=40)

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Institution(BaseModel):
    id_institution = models.AutoField(_('Institution ID'), primary_key=True)
    name = models.CharField(_('Name'), max_length=40)

    class Meta:
        db_table = 'institution'
        verbose_name = _('Institution')
        verbose_name_plural = _('Instituitions')

    def __str__(self):
        return self.name


class Formation(BaseModel):
    id_formation = models.AutoField(_('Formation ID'), primary_key=True)
    name = models.CharField(_('Name'), max_length=100)
    workload = models.CharField(_('Workload'), max_length=40)
    curriculum_map = models.TextField(_('Curriculum Map'))
    start_date = models.DateTimeField(_('Start Date'))
    end_date = models.DateTimeField(_('End Date'))

    class Meta:
        db_table = 'formation'
        verbose_name = _('Formation')
        verbose_name_plural = _('Formations')

    def __str__(self):
        return self.name
