# -*- coding: utf-8 -*-

from django import forms
from .models import ExpenseCategory, Expense, ExpenseItem


#===============================================================================
# Expense Category Form
#===============================================================================
class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        exclude = ('slug')

#===============================================================================
# Expense Form 
#===============================================================================
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ('slug', 'owner', 'status')


#===============================================================================
# Expense item
#===============================================================================
class ExpenseItemForm(forms.ModelForm):
    class Meta:
        model = ExpenseItem
        exclude = ('slug', 'expense')

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0:
            raise forms.ValidationError('Quantity should a positive number.')
        return quantity
