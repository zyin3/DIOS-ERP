# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Employee(models.Model):

    """ Model for Employee Information """

    user = models.ForeignKey(User, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    employee_id = models.PositiveIntegerField(unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'employee_profile'

        permissions = (
            # Permission    human-readable permission name
            ("can_approve", "Can approve expense submission"),
        )

    def __unicode__(self):
        return self.employee_id

    @models.permalink
    def get_absolute_url(self):
        return ('eclaim.humanresource.views.employee', (),
                {'employee_slug': self.slug})


class Department(models.Model):

    """ Department Model """

    name = models.CharField(unique=True, max_length=128)
    slug = models.SlugField(unique=True, max_length=128)
    members = models.ManyToManyField(User, through='Membership')

    class Meta:
        db_table = 'department'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('eclaim.humanresource.views.department', (),
                {'department_slug': self.slug})


<<<<<<< HEAD
    user = models.ForeignKey(User, unique=True)
    employee_id = models.PositiveIntegerField(_('employee_id'), unique=True)
#   department = models.ForeignKey(Department)
    title = models.CharField(_('job title'), blank=True, max_length=128)
#    is_admin = models.BooleanField(_('administrator status'), default=False)
=======
>>>>>>> 69261255e2b89ebadbd536d7610d8bdcd1593270

class Membership(models.Model):

    """ Department membership """

    user = models.ForeignKey(User, unique=True)
    department = models.ForeignKey(Department)
    is_manager = models.BooleanField(default=False)

    class Meta:
        db_table = 'membership'
