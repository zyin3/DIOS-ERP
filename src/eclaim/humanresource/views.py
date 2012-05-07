# -*- coding: utf-8 -*-

from django.http import HttpResponseNotAllowed, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.template.defaultfilters import slugify
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Employee, Department, Membership
from .forms import EmployeeForm, DepartmentForm


#===============================================================================
# Employee Views 
#===============================================================================
@login_required
def employees(request):
    """ Employee Factory Resource
    
    GET Get list of employee info        
    """

    if 'GET' == request.method:
        # get a new employee info
        employees = Employee.objects.all().order_by('employee_id')
        return HttpResponse(str(list('id: %d' % e.employee_id for e in employees)))

    else:
        raise HttpResponseNotAllowed


@csrf_protect
@login_required
@transaction.commit_on_success
def employees_create(request, template='humanresource/test_create_employee.html'):
    """ Employee Create Factory
    
    POST Create a employee
    GET Get a Create form
    """
    if 'POST' == request.method:
        # create a new employee info
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.user = request.user
            employee.slug = slugify(employee.employee_id)
            employee.save()

            dept = form.cleaned_data['department']
            is_manager = form.cleaned_data['is_manager']
            membership = Membership(user=request.user, department=dept, is_manager=is_manager)
            membership.save()

            return redirect(employee)

    elif 'GET' == request.method:
        form = EmployeeForm()

    template_param = {'form':form}
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))


@login_required
@transaction.commit_on_success
def employee(request, employee_slug):
    """ Employee Resource
        
    GET Get employee info with specified employee_id
    PUT Modify employee info 
    """
    if 'GET' == request.method:
        employee = get_object_or_404(Employee, slug=employee_slug)
        return HttpResponse('%s, %d' % (employee.user.username, employee.employee_id))

    elif 'PUT' == request.method:
        raise NotImplementedError

    elif 'DELETE' == request.method:
        employee = get_object_or_404(Employee, slug=employee_slug)
        employee.delete()
        return HttpResponse()

    else:
        raise HttpResponseNotAllowed


#===============================================================================
# Department Views 
#===============================================================================
@login_required
def departments(request, template=''):
    """ Departments
        
    GET Get list of department info
    """
    if 'GET' == request.method:
        dept_list = Department.objects.all().order_by('name')
        return HttpResponse(str(list(dept.name for dept in dept_list)))

    else:
        raise HttpResponseNotAllowed


@csrf_protect
@login_required
@transaction.commit_on_success
def departments_create(request, template='humanresource/test_create_employee.html'):
    """ Departments Factory
    
    POST Create a new department
    GET Get a Create form
    """
    if 'POST' == request.method:
        # create a new employee info
        form = DepartmentForm(request.POST)
        if form.is_valid():
            dept = form.save(commit=False)
            dept.slug = slugify(dept.name)
            dept.save()
            return redirect(dept)

    elif 'GET' == request.method:
        form = DepartmentForm()

    template_param = {'form':form}
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))


@login_required
@transaction.commit_on_success
def department(request, department_slug):
    """ Department Resource
        
    GET Get a department info with department_id    
    PUT Modify a department info
    """
    if 'GET' == request.method:
        dept = get_object_or_404(Department, slug=department_slug)
        return HttpResponse(dept.name)

    elif 'PUT' == request.method:
        raise NotImplementedError

    elif 'DELETE' == request.method:
        dept = get_object_or_404(Department, slug=department_slug)
        dept.delete()
        return HttpResponse()

    else:
        raise HttpResponseNotAllowed


