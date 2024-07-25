from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Sentiment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sentiments')
    review = models.TextField()

class Statistics(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='statistics')
    mean = models.FloatField()
    standard_deviation = models.FloatField()