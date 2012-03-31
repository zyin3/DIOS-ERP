# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('eclaim.humanresource.views',

    # get employee list
    url(r'^employee_list/$', 'employee_list_view'),

    # get employee info
    url(r'^employee/(?P<employee_id>\d+)/$', 'employee_detail_view'),

    # create an employee
    url(r'^create_employee/$', 'create_employee_view', name='create_employee_view'),

    # delete an employee (inactive)
    url(r'^delete_employee/$', 'delete_employee_view'),
)
