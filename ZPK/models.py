import datetime

from django.db import models
from django.utils import timezone
from django.db import models




class Worker(models.Model):
    LastName = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200)
    Age = models.DateField()
    Sallary = models.IntegerField()

    def __str__(self):
        return self.LastName + ' ' + self.FirstName



class PhoneBook(models.Model):
    ZpkPhoneInner = models.CharField(max_length=50,null=True,blank=True)
    ZpkPhoneOuter = models.CharField(max_length=50, null=True,blank=True)
    PrivatePhone = models.CharField(max_length=50,null=True,blank=True)
    FIO = models.CharField(max_length=200,null=True,blank=True)
    Doljnost = models.CharField(max_length=100,null=True,blank=True)
    Otdel = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        if self.FIO is None:
            return self.Doljnost
        else:
            return self.FIO
