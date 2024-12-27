from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, unique=True)
    lists = models.ManyToManyField('ShoppingList', related_name='lists', blank=True)
    current_list = models.ForeignKey(
        'ShoppingList',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"@{self.user_name}"


class ShoppingList(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=100)
    products = models.ManyToManyField('Product', related_name='shopping_lists', blank=True)
    users = models.ManyToManyField('User', related_name='users', blank=True)
    
    def __str__(self):
        return f"{self.list_name}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20, blank=True)
    count = models.IntegerField(default=0, blank=True)
    bought = models.BooleanField(blank=False)

    def __str__(self):
        return f"{self.product_name}"