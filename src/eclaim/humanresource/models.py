# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Department(models.Model):

    """ Department Model """

    name = models.CharField(unique=True, max_length=128)

    class Meta:
        db_table = 'department'

    def __unicode__(self):
        return u'%s(%s)' % (self.__class__.__name__, self.name)


class Employee(models.Model):

    """ Employee Model """

    user = models.ForeignKey(User, unique=True)
    employee_id = models.PositiveIntegerField(_('employee_id'), unique=True)
#   department = models.ForeignKey(Department)
    title = models.CharField(_('job title'), blank=True, max_length=128)
#    is_admin = models.BooleanField(_('administrator status'), default=False)


    class Meta:
        db_table = 'employee_profile'

        permissions = (
            # Permission    human-readable permission name
            ("can_approve", "Can approve expense submission"),
        )

    def __unicode__(self):
        return u'%s(id: %s)' % (self.__class__.__name__, self.employee_id)

