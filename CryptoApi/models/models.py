from django.db import models
from django.contrib.auth.models import User


class FirebaseToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)


class Pattern(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)


class Coin(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    current_price = models.FloatField(null=True, blank=True)


class TradingStrategy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patterns = models.ManyToManyField(Pattern)
    coins = models.ManyToManyField(Coin)
