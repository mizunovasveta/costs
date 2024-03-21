from django import forms
from .models import Expense



class ExpenseFilterForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    sort_by = forms.ChoiceField(choices=[
        ('', '------'),
        ('pub_date', 'Date'),
        ('-pub_date', 'Date (Descending)'),
        ('amount', 'Amount'),
        ('-amount', 'Amount (Descending)'),
        ('category', 'Category'),
        ('-category', 'Category (Descending)'),
    ], required=False)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'name', 'pub_date', 'amount', 'currency']
        widgets = {
            'pub_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date', 'id': 'datepicker'}),
        }

