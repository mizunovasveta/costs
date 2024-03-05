from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.forms import ModelForm
from .models import Expense
import requests
from django.urls import reverse_lazy
class Index(ListView):
    model = Expense
    template_name = "polls/index.html"
    context_object_name = "latest_expense_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        pub_date = self.request.GET.get('pub_date')
        if pub_date:
            queryset = queryset.filter(pub_date=pub_date)
        return queryset

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
