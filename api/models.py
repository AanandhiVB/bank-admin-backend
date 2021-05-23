from django.db import models

# Create your models here.

class Bank(models.Model):
    name     = models.CharField(max_length=100, blank=False, null=False)
       

class Branch(models.Model):
    bank     = models.ForeignKey(Bank,on_delete=models.CASCADE)
    ifsc     = models.CharField(max_length=100, blank=False, null=False)
    branch   = models.CharField(max_length=100, blank=False, null=False)
    address  = models.CharField(max_length=200, blank=False, null=False)
    city     = models.CharField(max_length=100, blank=False, null=False)
    district = models.CharField(max_length=100, blank=False, null=False)
    state    = models.CharField(max_length=100, blank=False, null=False)
    
    
