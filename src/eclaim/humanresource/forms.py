# -*- coding: utf-8 -*-

from django import forms
from .models import Employee, Department


class EmployeeForm(forms.ModelForm):

    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label='------')
    is_manager = forms.BooleanField()

    class Meta:
        model = Employee
        exclude = ('user', 'slug')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ('members', 'slug')
