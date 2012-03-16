# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_protect
from eclaim.expense.models import ExpenseType
from django.utils.simplejson import dumps
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# require login
def expense_package_view(request):
    pass

# require login
def expense_list_view(request):
    pass

# require login
def expense_detail_view(request):
    pass

# require login
def create_expense_view(request):
    # new expense status: draft
    template = loader.get_template("expense/newExpense.html");
    context = RequestContext (request, {});
    return HttpResponse(template.render(context));

# require login
def delete_expense_view(request):
    # do not do real delete, inactivate it
    pass

# require login
def update_expense_view(request):
    pass

# require login
def submit_expense_view(request):
    pass

# require login and has approval right
def approve_expense_view(request):
    pass



# expense type view
# This view includes get, sort, delete functionality.
@csrf_protect
def expense_type_view(request):
    #request method is 'POST', then insert/update or delete the expense Type record
    if request.method == 'POST':
        #if it is a delete request
        if request.POST.get('oper') == 'del':
            del_ID = request.POST.get('id')
            #find the object accroding to id, and delete it
            ExpenseType.objects.get(type__iexact=del_ID).delete();
            return HttpResponse()
        #it is a insert/update request
        expenseTypeValue = request.POST.get('expenseType')
        expenseLimitValue = request.POST.get('expenseLimit')
        commentsValue = request.POST.get('comments')
        #insert/update
        #insert using lower case, e.g. 'taxi' and 'Taxi' has same primary key
        row = ExpenseType(typename=expenseTypeValue.lower(),
                          limit=expenseLimitValue,
                          comments=commentsValue,);
        row.save();
        return HttpResponse()
    #request method is GET
    #calculate pager
    pageNum = int(request.GET.get('page'))
    rowNum = int(request.GET.get('rows'))
    sortName = request.GET.get('sidx') #sort name
    if(request.GET.get('sord') == 'desc'): #desc or asc
        sortName = '-' + sortName
    expenseList = ExpenseType.objects.all().order_by(sortName)
    paginator = Paginator(expenseList, rowNum)
    try:
        expensePageList = paginator.page(pageNum)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        expensePageList = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        expensePageList = paginator.page(paginator.num_pages)

    #dump them to json string
    listJSON = []
    #print(listJSON)
    for item in expensePageList.object_list:
        item_dict = {
          "expenseType": item.pk.title(),
          "expenseLimit": item.limit,
          "comments": item.comments,
        }
        listJSON.append(item_dict)
    response = {
        "total": paginator.num_pages,
        "records": paginator.count,
        "page": pageNum,
        "row":listJSON
       }
    return HttpResponse(dumps(response), content_type='application/json; charset=utf8')
