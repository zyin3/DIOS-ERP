# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    #create user
    url(r'^user/$', 'eclaim.humanresource.views.create_employee_view'),

)
