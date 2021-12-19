from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    id_category = models.AutoField(_("Category ID"), primary_key=True)
    name = models.CharField(_("Name"), max_length=40)

    def __str__(self):
        return self.name
