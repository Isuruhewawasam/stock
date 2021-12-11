from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Catogory(models.Model):
    cat_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    product_cat = models.ForeignKey(Catogory,on_delete=models.CASCADE)
    product_Created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image")
    product_price = models.PositiveIntegerField()
    suppler_price = models.PositiveIntegerField()
    sale_price = models.PositiveIntegerField()
    stock_contity =models.PositiveIntegerField()
    discriptions = models.TextField()
    worrenty = models.CharField(null=True,blank=True,max_length=100)
    return_policy = models.CharField(null=True,blank=True,max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
