from django.db import models
from django.contrib.auth import  get_user_model
from datetime import datetime
from django.contrib.auth import get_user_model
User=get_user_model()

class user_details(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class category(models.Model):
    category_type=models.CharField(max_length=100)

class District(models.Model):
    name=models.CharField(max_length=100)


class owner(models.Model):
     fname=models.CharField(max_length=100)
     lname=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     mobile=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     username=models.CharField(max_length=100)
     password=models.CharField(max_length=100)
     document=models.FileField(upload_to="owner_documets")
     status=models.CharField(max_length=100)


class land_property(models.Model):
    place=models.CharField(max_length=100)
    category=models.ForeignKey(category,on_delete=models.DO_NOTHING)
    price=models.FloatField()
    area=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    district=models.ForeignKey(District,on_delete=models.DO_NOTHING)
    owner=models.ForeignKey(owner,on_delete=models.CASCADE)
    photo1=models.ImageField(upload_to="land")
    photo2=models.ImageField(upload_to="land")

class house_and_appartments(models.Model):
     place=models.CharField(max_length=100)
     category=models.ForeignKey(category,on_delete=models.DO_NOTHING)
     price=models.CharField(max_length=100)
     area=models.CharField(max_length=100)
     address=models.CharField(max_length=100)
     bedroom=models.CharField(max_length=100)
     bathroom=models.CharField(max_length=100)
     furnished=models.CharField(max_length=100)
     description=models.CharField(max_length=300)
     district=models.ForeignKey(District,on_delete=models.DO_NOTHING)
     owner=models.ForeignKey(owner,on_delete=models.CASCADE)
     photo1=models.ImageField(upload_to="house")
     photo2=models.ImageField(upload_to="house")





class Admin(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


class Favorites(models.Model):
    user= user=models.ForeignKey(User,on_delete=models.CASCADE)
    land=models.ForeignKey(land_property,on_delete=models.CASCADE,null=True)
    house=models.ForeignKey(house_and_appartments,on_delete=models.CASCADE,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
     
     
     
     




    