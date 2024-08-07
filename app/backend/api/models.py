from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    # Every Company has a reverse relationship to a User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sentiment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sentiments')
    review = models.TextField()
    sentiment_score = models.FloatField()
    # created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return f"Sentiment for {self.company.name}"
    

class Statistics(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='statistics')
    mean_sentiment = models.FloatField(default=0.0)
    sentiment_count = models.IntegerField(default=0)
    positive_sentiment_count = models.IntegerField(default=0)
    negative_sentiment_count = models.IntegerField(default=0)
    neutral_sentiment_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Statistics for {self.company.name}"