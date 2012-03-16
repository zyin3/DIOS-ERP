# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Employee(models.Model):

    """ Employee Model """

    user = models.OneToOneField(User, unique=True)
    first_name = models.CharField(_('first name'), blank=False, max_length=128)
    middle_name = models.CharField(_('middle name'), blank=True, max_length=128)
    last_name = models.CharField(_('last name'), blank=False, max_length=128)
    email = models.EmailField(_('e-mail address'), blank=False)
    is_admin = models.BooleanField(_('administrator status'), default=False)
    title = models.CharField(_('job title'), blank=True, max_length=128)

    class Meta:
        db_table = 'employee'

        permissions = (
            # Permission    human-readable permission name
            ("can_approve", "Can approve expense submission"),
        )

    #def __str__(self):
        #return 'User: %s' % self.user.username
