from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.forms import ModelForm
from .models import Expense
import requests
from django.urls import reverse_lazy
from django.db.models import Sum
class Index(ListView):
    model = Expense
    template_name = "polls/index.html"
    context_object_name = "latest_expense_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(pub_date__range=[start_date, end_date])
        elif start_date:
            queryset = queryset.filter(pub_date__range=[start_date, start_date])
        elif end_date:
            queryset = queryset.filter(pub_date__lte=end_date)
        sort_by = self.request.GET.get('sort_by')
        if sort_by is not None:
            queryset = queryset.order_by('pub_date')
            if sort_by == 'pub_date':
                queryset = queryset.reverse()
        sort_by_amount = self.request.GET.get('sort_by_amount')
        if sort_by_amount is not None:
            queryset = queryset.order_by('amount')
            if sort_by_amount == 'amount':
                queryset = queryset.reverse()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_amount = self.get_queryset().aggregate(total_amount=Sum('amount'))['total_amount']
        if total_amount is None:
            total_amount = 0
        context['total_amount'] = total_amount
        context['start_date'] = self.request.GET.get('start_date')
        context['end_date'] = self.request.GET.get('end_date')
        return context

class Detail(DetailView):
    model = Expense
    template_name = "polls/detail.html"

class ExpenseModelForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'name', 'pub_date', 'amount', 'currency']

class Update(UpdateView):
    model = Expense
    form_class = ExpenseModelForm
    template_name = 'polls/update.html'

    def get_success_url(self):
        return reverse_lazy('polls:detail', kwargs={'pk': self.object.pk})

class Create(CreateView):
    model = Expense
    fields = ['category', 'name', 'pub_date', 'amount', 'currency']
    template_name = 'polls/create.html'
    success_url = reverse_lazy('polls:index')

class Delete(DeleteView):
    model = Expense
    template_name = 'polls/delete.html'
    success_url = reverse_lazy('polls:index')


    # def load_currencies():
#     url = "https://exchange-rates.abstractapi.com/v1/live"
#     response = requests.request("GET", url)
#     print(response.text)
#     data = json.loads(response.text)
#     data["exchange_rates"].keys()
