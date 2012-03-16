# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    #new expense report
    url(r'^new_expense/$', 'eclaim.expense.views.create_expense_view'),
    url(r'^expense_type/$', 'eclaim.expense.views.expense_type_view'),
)
