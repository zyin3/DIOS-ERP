# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class ExpensePackage(models.Model):

    """ Expense Package Model 

    name = models.CharField(_('package name'), max_length=128)
    owner = models.ForeignKey(User)
    created = models.DateTimeField(_('created date'), auto_now_add=True)
    modified = models.DateTimeField(_('last modified date'), auto_now=True)"""

    class Meta:
        db_table = 'expense_package'


EXPENSE_CATEGORY_LUNCH = 0
EXPENSE_CATEGORY_HOTEL = 1
EXPENSE_CATEGORY_CHOICES = (
    (EXPENSE_CATEGORY_LUNCH, 'lunch'),
    (EXPENSE_CATEGORY_HOTEL, 'hotel')
                            )

EXPENSE_STATUS_DRAFT = 0
EXPENSE_STATUS_SUBMITTED = 1
EXPENSE_STATUS_APPROVED = 2
EXPENSE_STATUS_CHOICES = (
    (EXPENSE_STATUS_DRAFT, 'draft'),
    (EXPENSE_STATUS_SUBMITTED, 'submitted'),
    (EXPENSE_STATUS_APPROVED, 'approved'),
                            )

class ExpenseItem(models.Model):

    """ Expense Item Model 

    category = models.PositiveSmallIntegerField('expense category', choices=EXPENSE_CATEGORY_CHOICES, default=0)
    amount = models.FloatField('amount', null=False)
    status = models.PositiveSmallIntegerField('expense status', choices=EXPENSE_STATUS_CHOICES, default=0)
    package = models.ForeignKey(ExpensePackage, unique=True)
    date = models.DateTimeField('date')
    created = models.DateTimeField('created date', auto_now_add=True)
    modified = models.DateTimeField('last modified date', auto_now=True)
    location = models.ForeignKey('location', null=False)"""

    class Meta:
        db_table = 'expense_item'
        
        
""" Define the expense type and their limit"""
class ExpenseType(models.Model):

    """ Expense Type Model """
    #expense type
    type = models.CharField('expense type',max_length=100,primary_key='true')
    #expense limit
    limit = models.IntegerField('expense limit')
    #expense comments
    comments = models.TextField('expense comments')
    class Meta:
        db_table = 'expense_type'

