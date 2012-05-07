# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('eclaim.humanresource.views',

    # employees/ 
    # GET: list employees  
    url(r'^employees/$', 'employees'),

    # employees/create/
    # POST: add a new employee
    # GET: get a create form
    url(r'^employees/create/$', 'employees_create'),

    # employees/xxx/
    # GET: get a employee detail
    # PUT: update employee xxx
    # DEL: delete an employee
    url(r'^employee/(?P<employee_slug>[-\w]+)/$', 'employee'),

    # departments/ 
    # GET: all departments  
    url(r'^departments/$', 'departments'),

    # departments/create/
    # POST: add a new department
    url(r'^departments/create/', 'departments_create'),

    # departments/xxx/
    # GET: get a department detail
    # PUT: update department xxx
    # DEL: delete a department
    url(r'^department/(?P<department_slug>[-\w]+)/$', 'department'),
)

