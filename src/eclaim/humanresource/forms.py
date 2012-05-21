# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from .models import Employee


USER_ACTIVE_CHOICES = (('true', 'Active User'), ('false', 'Inactive User'))
class EmployeeForm(forms.ModelForm):

    email = forms.EmailField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())
    confirm = forms.CharField(max_length=32, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    #title = forms.CharField(max_length=32)
    is_active = forms.BooleanField()

    class Meta:
        model = Employee
        fields = ['password', 'confirm', 'first_name',
                  'last_name', 'employee_id',
#                 'department',
                  'email',
                  'is_active']

    def clean(self):
        data = self.cleaned_data
        password = data.get('password', None)
        confirm = data.get('confirm', None)

        if password and confirm and password == confirm:
            return data
        else:
            raise forms.ValidationError('Please comfirm the password!')

    def save(self):
        data = self.cleaned_data
        print data
        user = User.objects.create_user(data['email'],
                                        data['email'],
                                        data['password'])
        user.first_name = data['first_name']
        # user.middle_name = data['middle_name']
        user.last_name = data['last_name']
        user.is_active = data['is_active']
        user.save()

        employee = Employee(user=user,
                            employee_id=data['employee_id'],
#                            department=data['department'],
                            #title=data['title'],
                            #is_admin=data['is_admin']
                            )
        employee.save()

        return employee