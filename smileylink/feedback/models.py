from django.db import models


class Account(models.Model):
    account_name = models.CharField(max_length=50)
    subscription_model = models.CharField(max_length=30)

    def __str__(self):
        return self.account_name

class Product(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_feedback = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
