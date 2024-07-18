from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

