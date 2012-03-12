# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    #new expense report
    url(r'^new_expense/$', 'eclaim.expense.views.create_expense_view'),
)
