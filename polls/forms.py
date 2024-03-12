from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'name', 'pub_date', 'amount', 'currency']
        widgets = {
            'pub_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'id': 'datepicker'}),
        }