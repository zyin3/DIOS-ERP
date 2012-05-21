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
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.format = '%d/%m/%Y'

        # at the same time, set the input format on the date field like you want it:
        self.fields['date'].input_formats = ['%d/%m/%Y']
