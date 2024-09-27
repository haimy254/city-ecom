from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 70)


    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField (max_length= 50)
    last_name = models.CharField (max_length= 50)
    phone = models.IntegerField ()
    email = models.EmailField (max_length= 30)
    password =models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name =models.CharField (max_length= 50)
    price = models.IntegerField (default = 0)
    image = models.ImageField(upload_to='uploads/product/')
    category = models.ForeignKey (Category, on_delete=models.CASCADE, default = 1)
    description = models.CharField (max_length= 250, blank=True, default='', null=True)

    #add sales stuffs
    is_sales = models.BooleanField(default=False)
    sales_price = models.IntegerField (default = 0)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,  on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length= 50,blank=True, default='')
    phone = models.IntegerField (blank=True, default='')
    date = models.DateTimeField(default= datetime.datetime.today)
    stauts = models.BooleanField(default=False)

    def __str__(self):
        return self.product