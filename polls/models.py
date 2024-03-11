from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    # CATEGORY_CHOICES = [
    #     ('markets', 'Markets'),
    #     ('pharmacy', 'Pharmacy'),
    #     ('entertainment', 'Entertainment'),
    #     ('bookstore', 'Bookstore'),
    #     ('electronics and gadgets', 'Electronics and gadgets'),
    #     ('appliances', 'Appliances'),
    #     ('beauty', 'Beauty'),
    #     ('wellness', 'Wellness')
    # ]
    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField("date published")
    amount = models.FloatField(default=0.00)
    currency = models.CharField(max_length=3, default='USD')

    def __str__(self):
        return self.name
