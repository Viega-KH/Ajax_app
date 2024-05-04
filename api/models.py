#models.py
from django.db import models



class Order(models.Model):
    name = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    addres = models.TextField()
    liter = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name