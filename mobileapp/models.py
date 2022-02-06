from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class usertype(models.Model):
    type=models.CharField(max_length=30)

class customer(models.Model):
    usertype=models.ForeignKey(usertype,on_delete=CASCADE)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30,null=True,blank=True)
    mobile=models.BigIntegerField()
    gender=models.CharField(max_length=30)
    dob=models.DateField()
    address=models.TextField(max_length=300)
    country=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    login=models.ForeignKey(User,on_delete=CASCADE)
    otp=models.IntegerField()

    def __str__(self):
        return self.fname

class reseller(models.Model):
    usertype=models.ForeignKey(usertype,on_delete=CASCADE)
    companyname=models.CharField(max_length=30)
    companyid=models.CharField(max_length=30)
    bankholder=models.CharField(max_length=30)
    bankaccountnumber=models.CharField(max_length=30)
    bankaccountifsc=models.CharField(max_length=30)
    address=models.TextField(max_length=300)
    mobile=models.BigIntegerField()
    country=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    login=models.ForeignKey(User,on_delete=CASCADE)
    requestdate=models.DateField(default=timezone.now)
    otp=models.IntegerField()
    
    def __str__(self):
        return self.companyname
