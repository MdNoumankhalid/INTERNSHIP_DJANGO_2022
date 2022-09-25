from django.db import models


class UserLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype = models.CharField(max_length=30)


class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


class AddProduct(models.Model):
    cat_name = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50, null=True)
    uom = models.CharField(max_length=30,null=True)
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    image = models.CharField(max_length=1000, null=True)
    total_stock = models.IntegerField(null=True)


class AddCategory(models.Model):
    cat_name = models.CharField(max_length=50, null=True)


class MyOrder(models.Model):
    user_id = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50, null=True)
    quantity = models.CharField(max_length=50, null=True)
    unit_price = models.CharField(max_length=50, null=True)
    total = models.CharField(max_length=50, null=True)
    order_status = models.CharField(max_length=50, null=True)
    payment_status = models.CharField(max_length=50, null=True)


class AddPayment(models.Model):
    order_id = models.CharField(max_length=50, null=True)
    user_id = models.CharField(max_length=50, null=True)
    payment_date = models.CharField(max_length=50, null=True)
    paid_amount = models.CharField(max_length=50, null=True)


class AddStock(models.Model):
    pid = models.CharField(max_length=50, null=True)
    stock = models.CharField(max_length=50, null=True)


class AddFeedback(models.Model):
    user_id = models.CharField(max_length=50, null=True)
    about_product = models.CharField(max_length=50, null=True)
    about_service = models.CharField(max_length=50, null=True)
    comments = models.CharField(max_length=50, null=True)


class OtpCode(models.Model):
    otp = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
