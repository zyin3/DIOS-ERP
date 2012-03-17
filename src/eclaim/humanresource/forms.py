# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from .models import Employee

class EmployeeForm(forms.ModelForm):

    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput())
    confirm = forms.CharField(max_length=32, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=32)
    middle_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=32)

    class Meta:
        model = Employee
        fields = ['username', 'password', 'confirm', 'first_name',
                  'middle_name', 'last_name', 'employee_id',
#                  'department',
                  'email', 'title', 'is_admin']

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
        user = User.objects.create_user(data['username'],
                                        data['email'],
                                        data['password'])
        user.first_name = data['first_name']
        user.middle_name = data['middle_name']
        user.last_name = data['last_name']
        user.save()

        employee = Employee(user=user,
                            employee_id=data['employee_id'],
#                            department=data['department'],
                            title=data['title'],
                            is_admin=data['is_admin']
                            )
        employee.save()

        return employee
