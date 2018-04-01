from django.db import models

# Create your models here.


class User(models.Model):
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField


class Lot(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    image = models.ImageField
    start_date = models.DateTimeField
    end_date = models.DateTimeField
    status = models.CharField(max_length=8)


class Bet(models.Model):
    user = models.CharField(max_length=40)
    lot_name = models.CharField(max_length=40)
    bet_time = models.DateTimeField
    amount = models.FloatField
