from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from dealership.models import *

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(13)], max_length=13)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return str(self.user)
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    car_dealer = models.ForeignKey(CarDealer, on_delete=models.PROTECT)
    rent = models.CharField(max_length=8)
    vehicle = models.CharField(Vehicles, on_delete=models.PROTECT)
    days = models.CharField(max_length=3)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.is_complete)
    