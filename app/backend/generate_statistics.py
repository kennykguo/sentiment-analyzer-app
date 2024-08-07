import os
import django
from django.db.models import Count
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from api.models import Company, Sentiment, Statistics

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon', quiet=True)

def generate_statistics():
    sia = SentimentIntensityAnalyzer()

    for company in Company.objects.all():
        sentiments = Sentiment.objects.filter(company=company)
        
        stats, _ = Statistics.objects.get_or_create(company=company)
        
        stats.sentiment_count = sentiments.count()
        
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        total_sentiment = 0

        for sentiment in sentiments:
            sentiment_score = sia.polarity_scores(sentiment.review)['compound']
            total_sentiment += sentiment_score

            if sentiment_score > 0.05:
                positive_count += 1
            elif sentiment_score < -0.05:
                negative_count += 1
            else:
                neutral_count += 1

        stats.mean_sentiment = total_sentiment / stats.sentiment_count if stats.sentiment_count > 0 else 0.0
        stats.positive_sentiment_count = positive_count
        stats.negative_sentiment_count = negative_count
        stats.neutral_sentiment_count = neutral_count
        
        stats.save()
        
        print(f"Generated statistics for company ID: {company.id}")

if __name__ == "__main__":
    generate_statistics()