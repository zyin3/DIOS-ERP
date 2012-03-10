# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import Context, loader,RequestContext

def employee_login_view(request):
    """ Login """
    pass


def employee_logout_view(request):
    """ Logout """
    pass


# require login and admin
def employee_list_view(request):
    """ Lists a batch of the employees """
    pass

# require login and admin
def employee_detail_view(request):
    """ Gives Detail information of an employee """
    pass

# require login
def employee_info_view(request):
    """ Gives simple information of an employee """
    pass

# requrie login and admin
def create_employee_view(request):
    """ Creates a employee """
    indexTemplate = loader.get_template("humanresource/user.html");
    context = Context({});
    return HttpResponse(indexTemplate.render(context));
    pass

# require login and admin
def delete_employee_view(request):
    """ Deletes a employee """
    pass

# require login on updating oneself
# require login and admin on updating others
def update_employee(request):
    pass
