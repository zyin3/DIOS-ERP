# -*- coding: utf-8 -*-

import decimal

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class ExpenseCategory(models.Model):

    """ Expense Type Model
    
    Define the expense type and their limit 
    """

    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), max_length=64, unique=True)
    limit = models.IntegerField(_('amount limit'))
    description = models.TextField(_('description'))

    class Meta:
        db_table = 'expense_category'

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('eclaim.expense.views.expense_category', (), {'category_slug': self.slug})


class Expense(models.Model):

    """ Expense Package Model """

    STATUS_DRAFT = 0
    STATUS_SUBMITTED = 1
    STATUS_APPROVED = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'draft'),
        (STATUS_SUBMITTED, 'submitted'),
        (STATUS_APPROVED, 'approved'),
                                )

    STATUS_CHOICES_DICT = dict(draft=STATUS_DRAFT,
                               submitted=STATUS_SUBMITTED,
                               approved=STATUS_APPROVED,)

    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), max_length=64, unique=True)
    owner = models.ForeignKey(User)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_DRAFT)
    created = models.DateTimeField(_('created date'), auto_now_add=True)
    modified = models.DateTimeField(_('modified date'), auto_now=True)
    description = models.TextField(_('description'))

    class Meta:
        db_table = 'expense'

    def __unicode__(self):
        return '%s(%s, %s, %.2f)' % (self.__class__.__name__,
                                     self.name,
                                     self.status,
                                     self.total
                                     )

    @property
    def total(self):
        """ Total price of expense """
        total_price = decimal.Decimal('0.00')
        expense_items = ExpenseItem.objects.filter(expense=self)
        for item in expense_items:
            total_price += item.total
        return total_price

    @property
    def item_number(self):
        """ Number of expense items """
        item_num = ExpenseItem.objects.filter(expense=self).count()
        return item_num

    @models.permalink
    def get_absolute_url(self):
        return ('eclaim.expense.views.expense', (), {'expense_slug': self.slug})


class ExpenseItem(models.Model):

    """ Expense Item Model """

    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), max_length=64, unique=True)
    quantity = models.IntegerField(_('quantity'), default=1)
    price = models.DecimalField(_('price'), max_digits=9, decimal_places=2)
    expense = models.ForeignKey(Expense)
    category = models.ForeignKey(ExpenseCategory)
    date = models.DateTimeField(_('date'))
    description = models.TextField(_('description'))

    class Meta:
        db_table = 'expense_item'

    def __unicode__(self):
        return '%s(%s, %s, %s, %.2f)' % (self.__class__.__name__,
                                     self.name,
                                     self.category.name,
                                     self.quantity,
                                     self.price
                                     )

    @property
    def total(self):
        """ total price of expense item """
        return self.price * self.quantity

    @property
    def category_name(self):
        """ expense category """
        return self.category.name

    @models.permalink
    def get_absolute_url(self):
        return ('eclaim.expense.views.expense_item', (), {'expense_slug': self.expense.slug,
                                                          'item_slug': self.slug})
