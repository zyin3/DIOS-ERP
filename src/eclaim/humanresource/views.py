# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core import serializers
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

from .models import Employee
from .forms import EmployeeForm

# require login and admin
def employee_list_view(request):
    """ Lists a batch of the employees """
    employees = Employee.objects.all().order_by("employee_id")

    # rows to display in one page
    page_rows = int(request.GET.get("page_rows", '10'))
    paginator = Paginator(employees, page_rows)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        employees = paginator.page(page)
    except (InvalidPage, EmptyPage):
        employees = paginator.page(paginator.num_pages)

    response = HttpResponse()
    serializers.serialize('json',
                          employees.object_list,
                          ensure_ascii=False,
                          fields=('employee_id',
                                  'first_name',
                                  'last_name',
                                  'is_admin'),
                          stream=response)
    return response


# require login and admin
def employee_detail_view(request, employee_id):
    """ Gives Detail information of an employee """
    employee = Employee.objects.get(employee_id=employee_id)

    response = HttpResponse()
    serializers.serialize('json', [employee, ], ensure_ascii=False, stream=response)
    return response


# requrie login and admin
@csrf_protect
def create_employee_view(request):
    """ Creates an employee """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return HttpResponseRedirect('../employee/%d/' % employee.employee_id)
    else:
        form = EmployeeForm()

    return render_to_response('humanresource/test_create_employee.html',
                               {'form': form},
                               context_instance=RequestContext(request),
                               )


# require login and admin
def delete_employee_view(request, employee_id):
    """ Deletes a employee """
    pass

# require login on updating oneself
# require login and admin on updating others
def update_employee(request):
    pass


