from django.test import TestCase
from .models import Expense, Category, Currency
from django.contrib.auth.models import User

class CategoryModelTest(TestCase):
    def test_get(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")

class CurrencyModelTest(TestCase):
    def test_get(self):
        сurrency = Currency.objects.create(name="Test Currency")
        self.assertEqual(сurrency.name, "Test Currency")

class UserModelTest(TestCase):
    def test_get(self):
        user = User.objects.create(username='testuser')
        self.assertEqual(user.username, "testuser")

class ExpenseModelTest(TestCase):
    def test_get(self):
        self.user = User.objects.create(username="testuser")
        self.сurrency = Currency.objects.create(name="Test Currency")
        self.category = Category.objects.create(name="Test Category")
        self.expense = Expense.objects.create(
            user = self.user,
            name = "Test Expense",
            category = self.category,
            pub_date = "2024-06-24",
            amount = 100.00,
            currency =self.сurrency)
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.сurrency.name, "Test Currency")
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.expense.name, "Test Expense")
        self.assertEqual(self.expense.amount, 100.00)
        self.assertEqual(self.expense.pub_date, "2024-06-24")
