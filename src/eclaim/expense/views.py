# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import Context, loader,RequestContext
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
    context = RequestContext (request,{});
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
