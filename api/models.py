from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    discount = models.DecimalField(decimal_places=2, max_digits=5)
    shipping_cost = models.DecimalField(decimal_places=2, max_digits=10)
    ref = models.CharField(max_length=10)


class Order(models.Model):
    date_of_sales = models.DateField()
    payment_method = models.CharField()
    region_of_sales = models.CharField()
    customer = models.ForeignKey(Customer, db_index=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, db_index=True, on_delete=models.CASCADE)
    ref = models.CharField(max_length=10)
