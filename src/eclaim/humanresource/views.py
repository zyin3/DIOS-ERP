# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage,PageNotAnInteger
from django.core import serializers
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.utils.simplejson import dumps


from .models import Employee
from .forms import EmployeeForm

# require login and admin
def employee_list_view(request):
    """ Lists a batch of the employees """

    pageNum = int(request.GET.get('page'))
    rowNum = int(request.GET.get('rows'))
    sortName = request.GET.get('sidx') #sort name
    if(request.GET.get('sord') == 'desc'): #desc or asc
        sortName = '-' + sortName
    employees = Employee.objects.all().order_by("employee_id")
    paginator = Paginator(employees, rowNum)
    try:
        employees = paginator.page(pageNum)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)


    #dump them to json string
    listJSON = []
    #print(listJSON)
    for item in employees.object_list:
        item_dict = {
          "employee_id":item.employee_id,
          "first_name": item.user.first_name,
          "last_name": item.user.last_name,
          "is_active": item.user.is_active,
        }
    listJSON.append(item_dict)
    response = {
        "total": paginator.num_pages,
        "records": paginator.count,
        "page": pageNum,
        "row":listJSON
       }

    return HttpResponse(dumps(response), content_type='application/json; charset=utf8')


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

    return render_to_response('humanresource/create_employee.html',
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


