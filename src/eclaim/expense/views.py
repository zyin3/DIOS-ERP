# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .utils.template_param import common_parameter
from .models import ExpenseCategory, Expense
from .forms import ExpenseItemForm, ExpenseCategoryForm, ExpenseForm


#===============================================================================
# expense/xxx/
# expense/all/
#===============================================================================
@login_required
def expense(request, expense_slug):
    try:
        expense = request.user.expense_set.get(slug=expense_slug)
    except Exception as e:
        raise Http404('Expense %s not found' % expense_slug)
    else:
        return HttpResponse(str(expense))


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
        items = request.user.expense_set.get(slug=expense_slug) \
                        .expenseitem_set.all()
    except Exception as e:
        raise Http404('Expense items in expense %s not found' % expense_slug)
    else:
        return HttpResponse(str(list(str(i) for i in items)))


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
    categories = ExpenseCategory.objects.all()
    return HttpResponse(str(categories))


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
def create_expense_item(request, expense_slug, template='expense/test_expense.html'):
    # Get expense object
    expense = get_object_or_404(Expense, slug=expense_slug)

    if request.method == 'POST':
        form = ExpenseItemForm(request.POST)
        if form.is_valid():
            # set fields that is not in the form
            item = form.save(commit=False)
            item.slug = item.name
            item.expense = expense
            item.save()
            return redirect(item)
    else:
        form = ExpenseItemForm()

    template_param = common_parameter(head_title='create expense item', form=form)
    return render_to_response(template, template_param,
                              context_instance=RequestContext(request))


@csrf_protect
@login_required
@transaction.commit_on_success
def create_expense_category(request, template='expense/test_expense.html'):
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
