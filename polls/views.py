from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import ExpenseForm, ExpenseFilterForm, SignUpForm
from .models import Expense, Category, Currency
from django.urls import reverse_lazy
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import ExpenseSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class Index(ListView):
    model = Expense
    template_name = "polls/index.html"
    context_object_name = "latest_expense_list"
    login_url = '/polls/login/'

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Expense.objects.none()

        queryset = super().get_queryset().filter(user=self.request.user)
        form = ExpenseFilterForm(self.request.GET)

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            sort_by = form.cleaned_data.get('sort_by')

            if start_date and end_date:
                queryset = queryset.filter(pub_date__range=[start_date, end_date])
            elif start_date:
                queryset = queryset.filter(pub_date__gte=start_date)
            elif end_date:
                queryset = queryset.filter(pub_date__lte=end_date)

            if sort_by:
                queryset = queryset.order_by(sort_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        total_amount = queryset.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        context.update({
            'total_amount': total_amount,
            'filter_form': ExpenseFilterForm(self.request.GET),
        })
        return context

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:user_dashboard')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'polls/user_delete.html'
    success_url = reverse_lazy('polls:index')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)

class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'polls/user_dashboard.html'

class Detail(DetailView):
    model = Expense
    template_name = "polls/detail.html"

class Update(UpdateView):
    model = Expense
    template_name = 'polls/update.html'

    def get_success_url(self):
        return reverse_lazy('polls:detail', kwargs={'pk': self.object.pk})

class Create(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'polls/create.html'
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Delete(DeleteView):
    model = Expense
    template_name = 'polls/delete.html'
    success_url = reverse_lazy('polls:index')

class Create_category(CreateView):
    model = Category
    fields = ['name']
    template_name = 'polls/create_category.html'
    success_url = reverse_lazy('polls:index_category')

class Delete_category(DeleteView):
    model = Category
    template_name = 'polls/delete_category.html'
    success_url = reverse_lazy('polls:index_category')

class Update_category(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'polls/update_category.html'
    success_url = reverse_lazy('polls:index_category')

class Index_category(ListView):
    model = Category
    template_name = "polls/index_category.html"
    context_object_name = "category_list"

class Detail_category(DetailView):
    model = Category
    template_name = "polls/detail_category.html"

class Create_currency(CreateView):
    model = Currency
    fields = ['name']
    template_name = 'polls/create_currency.html'
    success_url = reverse_lazy('polls:index')
