from django.db import models
from django.contrib import admin


# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length=255)
    eemial = models.EmailField()
    econtact = models.CharField(max_length=255)
    econtact = models.CharField(max_length=255)

admin.site.register(Employee)
