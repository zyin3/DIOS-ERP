# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('eclaim.expense.views',
    url(r'^expense/(?P<expense_slug>[-\w]+)/$',
        'expense',
        name='expense'),

    url(r'^expense_item/(?P<item_slug>[-\w]+)/$',
        'expense_item',
        name='expense_item'),

    url(r'^expense_category/(?P<category_slug>[-\w]+)/$',
        'expense_category',
        name='expense_category'),

    url(r'^create_expense/$',
        'create_expense'),

    url(r'^create_expense_item/(?P<expense_slug>[-\w]+)/$',
        'create_expense_item'),

    url(r'^create_expense_category/$',
        'create_expense_category'),
)
