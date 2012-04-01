# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('eclaim.expense.views',

    # expense/create/ -> expense/xxx/
    # expense/xxx/item/create -> expense/xxx/item/yyy/
    # expense/category/create/ -> expense/category/zzz/
    url(r'^$', 'create_expense'),
    url(r'^(?P<expense_slug>[-\w]+)/item/$', 'create_expense_item'),
    url(r'^category/', 'create_expense_category'),

    # expense/all/
    # expense/xxx/
    url(r'^all/$', 'expense_all'),
    url(r'^(?P<expense_slug>[-\w]+)/$', 'expense'),

    # expense/xxx/item/all/
    # expense/xxx/item/yyy/
    url(r'^(?P<expense_slug>[-\w]+)/item/all/$', 'expense_item_all'),
    url(r'^(?P<expense_slug>[-\w]+)/item/(?P<item_slug>[-\w]+)/$', 'expense_item'),


    # expense/status/draft/
    # expense/status/submitted/
    # expense/status/approved/
    url(r'^status/draft/$', 'expense_status', {'status': 'draft'}),
    url(r'^status/submitted/$', 'expense_status', {'status': 'submitted'}),
    url(r'^status/approved/$', 'expense_status', {'status': 'approved'}),

    # expense/category/zzz/
    # expense/category/all/
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'expense_category'),
    url(r'^category/all/$', 'expense_category_all')
)










