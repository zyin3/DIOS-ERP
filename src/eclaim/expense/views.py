# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required

from .utils.template_param import common_parameter
from .utils.serializer import serialize_to_stream
from .models import ExpenseItem, ExpenseCategory, Expense
from .forms import ExpenseItemForm, ExpenseCategoryForm, ExpenseForm


@login_required
def expense(request, expense_slug, template='expense/test_expense.html'):
    expense = get_object_or_404(Expense, slug=expense_slug)
    return HttpResponse(str(expense))


@login_required
def expense_item(request, item_slug, tmplate='expense/test_expense.html'):
    item = get_object_or_404(ExpenseItem, slug=item_slug)
    return HttpResponse(str(item))


@login_required
def expense_category(request, category_slug, template='expense/test_expense.html'):
    category = get_object_or_404(ExpenseCategory, slug=category_slug)
    return HttpResponse(str(category))


@csrf_protect
@login_required
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
