from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField




class Ship (models.Model):

    Name = models.CharField(max_length=200)
    Photo = models.ImageField(upload_to='ships',null=True,blank=True)
    Info = models.CharField(max_length=2000,null=True,blank=True)
    Content = models.TextField(max_length=20000,null=True,blank=True)
    ContentEng = models.TextField(max_length=20000, null=True, blank=True)
    Pubdate = models.DateField(null=True,blank=True)


    def __str__(self):
        return self.Name



class Comment(models.Model):
    post = models.ForeignKey('logistic.Ship',on_delete=models.CASCADE)
    text = models.TextField()
    ContentExtended = models.TextField()





