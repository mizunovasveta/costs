from django.test import TestCase, Client
from django.urls import reverse
from .models import Expense, Category, Currency
from django.contrib.auth.models import User

class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(name="Test Category")
        self.currency = Currency.objects.create(name="USD")
        self.expense = Expense.objects.create(
            name ="Expense 1",
            amount=100.00,
            pub_date="2024-06-01",
            category=self.category,
            currency=self.currency,
            user=self.user
        )
        Expense.objects.create(
            name ="Expense 2",
            amount=200.00,
            pub_date="2024-06-15",
            category=self.category,
            currency=self.currency,
            user=self.user
        )
        Expense.objects.create(
            name ="Expense 3",
            amount=300.00,
            pub_date="2024-06-30",
            category=self.category,
            currency=self.currency,
            user=self.user
        )

    def test_filter_by_start_date_and_end_date_range(self):
        response = self.client.get(reverse("polls:index"),{'start_date': '2024-06-10', 'end_date': '2024-06-20'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Expense 2")
        self.assertNotContains(response, "Expense 1")
        self.assertNotContains(response, "Expense 3")

    def test_filter_by_start_date_range(self):
        response = self.client.get(reverse("polls:index"),{'start_date': '2024-06-10'})
        self.assertEqual(response.status_code,200)
        self.assertNotContains(response, "Expense 1")
        self.assertContains(response,"Expense 2")
        self.assertContains(response,"Expense 3")

    def test_filter_by_end_date_range(self):
        response = self.client.get(reverse("polls:index"),{'end_date': '2024-06-20'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "Expense 1")
        self.assertContains(response,"Expense 2")
        self.assertNotContains(response,"Expense 3")

    def test_sort_by_date(self):
        response = self.client.get(reverse("polls:index"), {'sort_by': 'date'})
        self.assertEqual(response.status_code, 200)
        expences = response.context['latest_expense_list']
        self.assertEqual(expences[0].name, "Expense 1")
        self.assertEqual(expences[1].name, "Expense 2")
        self.assertEqual(expences[2].name, "Expense 3")

    def test_sort_by_amount(self):
        response = self.client.get(reverse("polls:index"), {'sort_by': 'amount'})
        self.assertEqual(response.status_code, 200)
        expences = response.context['latest_expense_list']
        self.assertEqual(expences[0].name, "Expense 1")
        self.assertEqual(expences[1].name, "Expense 2")
        self.assertEqual(expences[2].name, "Expense 3")

    def test_sort_by_category(self):
        response = self.client.get(reverse("polls:index"), {'sort_by': 'category'})
        self.assertEqual(response.status_code, 200)
        expences = response.context['latest_expense_list']
        self.assertEqual(expences[0].name, "Expense 1")
        self.assertEqual(expences[1].name, "Expense 2")
        self.assertEqual(expences[2].name, "Expense 3")

    def test_amount(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        amount = response.context['total_amount']
        self.assertEqual(amount,600.00)







