from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    role_name=models.CharField(max_length=100,unique=True)
    status=models.CharField(max_length=20,choices=(('active','active'),('deactive','deactive')))

    def __str__(self):
        return self.role_name

class CustomUser(AbstractUser):
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.BigIntegerField()

