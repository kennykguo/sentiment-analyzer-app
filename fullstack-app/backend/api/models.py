from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    # Every Company has a reverse relationship to a User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sentiment(models.Model):
    # Every review has a reverse relationship to a Company
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sentiments')
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sentiment for {self.company.name}"


class Statistics(models.Model):
    # Every statistic has a reverse relationship to a Company
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='statistics')
    mean = models.FloatField()
    standard_deviation = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Statistics for {self.company.name}"