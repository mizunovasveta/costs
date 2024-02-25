from django.db import models

CATEGORY_CHOICES = [
    ('markets', 'Markets'),
    ('pharmacy', 'Pharmacy'),
    ('entertainment', 'Entertainment'),
    ('bookstore', 'Bookstore'),
    ('electronics and gadgets', 'Electronics and gadgets'),
    ('beauty', 'Beauty'),
    ('wellness', 'Wellness')
]

class Expense(models.Model):
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='-')
    name = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
    amount = models.FloatField(default=0.00)
    currency = models.CharField(max_length=3, default='USD')




