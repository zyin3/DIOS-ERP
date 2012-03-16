# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class EmployeeType(models.Model):

    """ Employee Type Model 

    title = models.CharField(_('title'), max_length=64)"""

    class Meta:
        db_table = 'employee_type'


class Employee(models.Model):

    """ Employee Model 

    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(_('first name'), blank=True, max_length=128)
    middle_name = models.CharField(_('middle name'), blank=True, max_length=128)
    last_name = models.CharField(_('last name'), blank=True, max_length=128)
    email = models.EmailField(_('e-mail address'), blank=True)
    is_admin = models.BooleanField(_('administrator status'), default=False)
    title = models.ForeignKey(EmployeeType)"""

    class Meta:
        db_table = 'employee'

    #def __str__(self):
        #return 'User: %s' % self.user.username