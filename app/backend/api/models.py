from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sentiment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sentiments')
    review = models.TextField()
    sentiment_score = models.FloatField()

    def __str__(self):
        return f"Sentiment for {self.company.name}"

class SentimentAnalysis(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sentiment_analyses', null=True)
    review = models.TextField()
    cleaned_review = models.TextField()
    vader_score = models.FloatField()
    model_prediction = models.CharField(max_length=20)
    avg_sentiment_score = models.FloatField()
    avg_word_count = models.FloatField()

    # Define fields for storing URLs of generated images
    def __str__(self):
        return f"Sentiment Analysis for {self.company.name}"

class NamedEntity(models.Model):
    sentiment_analysis = models.ForeignKey(SentimentAnalysis, related_name='entities', on_delete=models.CASCADE)
    entity_text = models.CharField(max_length=255)
    entity_label = models.CharField(max_length=100)
    count = models.IntegerField()

class Keyword(models.Model):
    sentiment_analysis = models.ForeignKey(SentimentAnalysis, related_name='keywords', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    count = models.IntegerField()

class POSTag(models.Model):
    sentiment_analysis = models.ForeignKey(SentimentAnalysis, related_name='pos_tags', on_delete=models.CASCADE)
    pos = models.CharField(max_length=20)
    word = models.CharField(max_length=100)
    count = models.IntegerField()

class AttentionWord(models.Model):
    sentiment_analysis = models.ForeignKey(SentimentAnalysis, related_name='attention_words', on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    count = models.IntegerField()