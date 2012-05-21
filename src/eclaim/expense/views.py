# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.serializers import serialize
from .utils.template_param import common_parameter
from .models import ExpenseCategory, Expense, ExpenseItem
from .forms import ExpenseItemForm, ExpenseCategoryForm, ExpenseForm

from django.utils.simplejson import dumps
from gviz_api import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#===============================================================================
# expense/xxx/
# expense/all/
#===============================================================================
@login_required
def expense(request, expense_slug, template='expense/newExpense.html'):
    try:
        expense = request.user.expense_set.get(slug=expense_slug)
        form = ExpenseItemForm()
    except Exception as e:
        raise Http404('Expense %s not found' % expense_slug)
    else:
        template_param = common_parameter(head_title='create expense item', expense=expense, form=form)
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))



@login_required
def expense_all(request):
    try:
        expense_set = request.user.expense_set.all()
    except Exception as e:
        raise Http404('Expense not found')
    else:
        return HttpResponse(str(list(str(exp) for exp in expense_set)))


#===============================================================================
# expense/xxx/item/yyy/
# expense/xxx/item/all/
#===============================================================================
@login_required
def expense_item(request, expense_slug, item_slug):
    try:
        item = request.user.expense_set.get(slug=expense_slug) \
                        .expenseitem_set.get(slug=item_slug)
    except Exception as e:
        raise Http404('Expense item %s in expense %s not found' % item_slug, expense_slug)
    else:
        return HttpResponse(str(item))


@login_required
def expense_item_all(request, expense_slug):
    try:
        items = request.user.expense_set.get(slug=expense_slug).expenseitems.all()
                        
        # serialize to google datatable format
        description = {"category": ("string", "Category"),
                   "date": ("date", "Date"),
                   "location": ("string", "Location"),
                   "price": ("number", "Price"),
                   "id": ("number", "Id"),
                   }
        """
        data = [{"name": "Mike", "salary": (10000, "$10,000"), "full_time": True},
            {"name": "Jim", "salary": (800, "$800"), "full_time": False},
            {"name": "Alice", "salary": (12500, "$12,500"), "full_time": True},
            {"name": "Bob", "salary": (7000, "$7,000"), "full_time": True}]
        """
        #dump them to json string
        data = []
        #print(listJSON)
        for item in items:
            item_dict = {
              "id":item.id,
              "date": item.date,
              "location": item.location,
              "price": float(item.price),
              "category": item.category.name
            }
            data.append(item_dict)
        data_table = DataTable(description)
        data_table.LoadData(data)
        print "Content-type: text/plain"
        print
        print data_table.ToJSon(columns_order=("id","category", "date", "location", "price"),order_by="id")

    except Exception as e:
        raise Http404(e)
    else:
        return HttpResponse(data_table.ToJSon(columns_order=("id","category", "date", "location", "price"),order_by="id"),content_type='application/json; charset=utf8')


#===============================================================================
# expense/status/draft/
# expense/status/submitted/
# expense/status/approved/
#===============================================================================
@login_required
def expense_status(request, status):
    try:
        stat = Expense.STATUS_CHOICES_DICT[status]
        expenses = request.user.expense_set.filter(status=stat)
    except Exception as e:
        raise Http404()
    else:
        return HttpResponse(str(list(str(exp) for exp in expenses)))


#===============================================================================
# 
#===============================================================================
@login_required
def expense_category(request, category_slug):
    category = get_object_or_404(ExpenseCategory, slug=category_slug)
    return HttpResponse(str(category))


@login_required
def expense_category_all(request):
    """ Return expense category in pages """
    pageNum = int(request.GET.get('page'))
    rowNum = int(request.GET.get('rows'))
    sortName = request.GET.get('sidx') #sort name
    if(request.GET.get('sord') == 'desc'): #desc or asc
        sortName = '-' + sortName
    category_list = ExpenseCategory.objects.all().order_by("name")
    paginator = Paginator(category_list, rowNum)
    try:
        categories = paginator.page(pageNum)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        categories = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        categories = paginator.page(paginator.num_pages)


    #dump them to json string
    listJSON = []
    #print(listJSON)
    for item in categories.object_list:
        item_dict = {
          "id":item.id,
          "name": item.name,
          "limit": item.limit,
          "description": item.description,
        }
    listJSON.append(item_dict)
    response = {
        "total": paginator.num_pages,
        "records": paginator.count,
        "page": pageNum,
        "row":listJSON
       }

    return HttpResponse(dumps(response), content_type='application/json; charset=utf8')


#===============================================================================
# views to create
#===============================================================================
@csrf_protect
@login_required
@transaction.commit_on_success
def create_expense(request, template='expense/test_expense.html'):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            # set fields that is not in the form
            expense = form.save(commit=False)
            expense.slug = expense.name
            expense.owner = request.user
            expense.save()
            return redirect(expense)
    else:
        form = ExpenseForm()

    template_param = common_parameter(head_title='create expense', form=form)
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))


@csrf_protect
@login_required
@transaction.commit_on_success
def create_expense_item(request, expense_slug, template='expense/newExpense.html'):
    # Get expense object
    expense = get_object_or_404(Expense, slug=expense_slug)
    if(len(request.POST['itemId'])!=0):
        expenseItem = ExpenseItem.objects.get(pk=int(request.POST['itemId']))
        form = ExpenseItemForm(request.POST, instance=expenseItem)
    else:
        form = ExpenseItemForm(request.POST)
    if form.is_valid():
        # set fields that is not in the form
        item = form.save(commit=False)
        #item.slug = item.name
        item.expense = expense
        item.save()
        return redirect(expense)
    else:
        form = ExpenseItemForm()

    template_param = common_parameter(head_title='create expense item', form=form, expense=expense)
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))


@csrf_protect
@login_required
@transaction.commit_on_success
def create_expense_category(request, template='expense/newExpense.html'):
    if request.method == 'POST':
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            # set fields that is not in the form
            category = form.save()
            category.slug = category.name
            category.save()
            return redirect(category)
    else:
        form = ExpenseCategoryForm()

    template_param = common_parameter(head_title='create expense category', form=form)
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))
    
#===============================================================================
# views to delete
#===============================================================================
@csrf_protect
@login_required
@transaction.commit_on_success
def delete_expense_item(request, expense_slug, itemId):
    try:        
        item = ExpenseItem.objects.get(pk=itemId)
        item.delete();
    except Exception as e:
        raise Http404('Expense Item not found') 
    else:
        return HttpResponse()
    
@csrf_protect
@login_required
@transaction.commit_on_success
def edit_expense_item(request, expense_slug, itemId, template='expense/expenseForm.html'):
    try:
        expense = request.user.expense_set.get(slug=expense_slug)
        item = ExpenseItem.objects.get(pk=itemId)
        form = ExpenseItemForm(instance=item)
    except Exception as e:
        raise Http404('Expense %s not found' % expense_slug)
    else:
        template_param = common_parameter(head_title='create expense item', expense=expense, form=form, item=item)
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))

