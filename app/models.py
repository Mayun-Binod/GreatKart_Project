from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
User=get_user_model()
STATE_CHOICES = [
    ('1', 'Koshi Province'),
    ('2', 'Madhesh Province'),
    ('3', 'Bagmati Province'),
    ('4', 'Gandaki Province'),
    ('5', 'Lumbini Province'),
    ('6', 'Karnali Province'),
    ('7', 'Sudurpashchim Province'),
]

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    locality=models.CharField(max_length=255)
    city=models.CharField(max_length=55)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=55)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES=[
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
]

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    product_image=models.ImageField(upload_to="product_img")


    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=[
    ('Accepted','accepted'),
    ('Packed','packed'),
    ('On The Way','on the way'),
    ('Delivered','delivered'),
    ('Cancel','cancel'),
]

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATE_CHOICES,default='Pending')

