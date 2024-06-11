from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=3, default='USD')
    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField("date published")
    amount = models.FloatField(default=0.00)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
