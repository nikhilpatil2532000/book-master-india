from django.db import models

# Create your models here.


class Story(models.Model):
    book_name = models.TextField()
    book_title = models.TextField()
    book_short_desc = models.TextField()
    book_long_desc = models.TextField()
    book_price = models.IntegerField()
    book_img = models.ImageField(upload_to='pics')
    book_publish_date = models.DateField()
    book_offers = models.BooleanField(default=False) 


class Historical(models.Model):
    book_name = models.TextField()
    book_title = models.TextField()
    book_short_desc = models.TextField()
    book_long_desc = models.TextField()
    book_price = models.IntegerField()
    book_img = models.ImageField(upload_to='pics')
    book_publish_date = models.DateField()
    book_offers = models.BooleanField(default=False) 


class Biography(models.Model):
    book_name = models.TextField()
    book_title = models.TextField()
    book_short_desc = models.TextField()
    book_long_desc = models.TextField()
    book_price = models.IntegerField()
    book_img = models.ImageField(upload_to='pics')
    book_publish_date = models.DateField()
    book_offers = models.BooleanField(default=False) 


class Contact(models.Model):
    contact_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70,default="")
    phone = models.CharField(max_length=70,default="")
    desc = models.CharField(max_length=500,default="")

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=10000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")