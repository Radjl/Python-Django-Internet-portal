import datetime


from django.utils import timezone
from django.db import models






class Inventory (models.Model):

    Name = models.CharField(max_length=200)
    Account = models.IntegerField(null=True,blank=True)
    Lifetime = models.IntegerField(null=True)
    Comissioning = models.DateField(null=True)
    MOL = models.CharField(max_length=200,null=True)
    InvNum = models.CharField(max_length=50,null=True)
    FactoryNum = models.CharField(max_length= 100,null=True)
    Location = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.Name



