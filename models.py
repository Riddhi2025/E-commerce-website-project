from django.db import models

# Create your models here.

class admindata(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.email

class sellerdata(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gst_number = models.IntegerField(null=True)
    pincode = models.IntegerField(null=True)
    def __str__(self):
        return self.email

class categorydata(models.Model):
    category = models.CharField(max_length=100,primary_key=True)
    total_products = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class itemdata(models.Model):
    image_url = models.CharField(max_length=100,null=True)
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    inventory_quantity = models.IntegerField()
    email_of_seller = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name


class customers(models.Model):
    Customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    def __str__(self):
        return self.name

class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    cart_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    email = models.CharField(max_length=100,null=True)
    total_price = models.IntegerField()
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class logindata(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class photodata(models.Model):
    email = models.CharField(max_length=100,primary_key=True)
    photo = models.CharField(max_length=100)
    def __str__(self):
        return self.email

class cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100,null=True)
    product_id = models.IntegerField()
    total_price = models.IntegerField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.email

