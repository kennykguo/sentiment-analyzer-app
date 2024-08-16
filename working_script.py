import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

import pandas as pd
import numpy as np
from collections import Counter
from django.db import transaction
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from api.models import Company, Sentiment, SentimentAnalysis, NamedEntity, Keyword, POSTag, AttentionWord
from modules.text_cleaning import clean_text
from modules.ner import perform_ner
from modules.pos_tagging import get_pos_tags, top_pos_tags
from modules.keyword_extraction import extract_keywords
from modules.plot_distribution import plot_sentiment_distribution, create_word_cloud

NUM_KEYWORDS = 30
NUM_NER = 20
COMPANY_ID = 1  # Set this to the ID of the company you want to analyze

def detect_emotions(reviews):
    analyzer = SentimentIntensityAnalyzer()
    scores = []
    for review in reviews:
        score = analyzer.polarity_scores(review)['compound']
        scores.append(score)
    return scores

def analyze_sentiments():
    print(f"Analyzing sentiments for company with ID: {COMPANY_ID}")
    
    try:
        company = Company.objects.get(id=COMPANY_ID)
    except Company.DoesNotExist:
        print(f"Error: Company with ID {COMPANY_ID} does not exist.")
        return

    sentiments = Sentiment.objects.filter(company=company)
    print(f"Found {sentiments.count()} sentiments for the company.")

    reviews = [sentiment.review for sentiment in sentiments]
    
    print("Cleaning reviews...")
    cleaned_reviews = [clean_text(review) for review in reviews]
    
    print("Detecting emotions...")
    vader_scores = detect_emotions(cleaned_reviews)

    print("Performing Named Entity Recognition...")
    entities = perform_ner(cleaned_reviews, NUM_NER)

    print("Performing POS Tagging...")
    pos_tags = get_pos_tags(cleaned_reviews)
    top_pos = top_pos_tags(pos_tags)
    print("\nTop POS Tags:")
    for pos in ['nouns', 'verbs', 'adjectives']:
        print(f"\nTop {pos.capitalize()}:")
        for word, count in top_pos[pos]:
            print(f"{word}: {count}")

    print("Extracting keywords...")
    keywords = extract_keywords(cleaned_reviews, NUM_KEYWORDS)

    print("Computing statistics...")
    avg_sentiment_score = np.mean(vader_scores)
    avg_word_count = np.mean([len(review.split()) for review in reviews])
    
    model_predictions = ['positive' if score > 0 else 'negative' for score in vader_scores]

    # all_top_words = []
    # top_attention_words = Counter(all_top_words).most_common(NUM_ATTENTION_WORDS)

    print("Saving analysis results to database...")
    with transaction.atomic():
        for i, sentiment in enumerate(sentiments):
            sentiment_analysis = SentimentAnalysis.objects.create(
                review=sentiment.review,
                cleaned_review=cleaned_reviews[i],
                vader_score=vader_scores[i],
                model_prediction=model_predictions[i],
                avg_sentiment_score=avg_sentiment_score,
                avg_word_count=avg_word_count,
            )

            for entity, count in entities:
                NamedEntity.objects.create(
                    sentiment_analysis=sentiment_analysis,
                    entity_text=entity[0],
                    entity_label=entity[1],
                    count=count,
                )

            for keyword, count in keywords:
                Keyword.objects.create(
                    sentiment_analysis=sentiment_analysis,
                    keyword=keyword,
                    count=count,
                )

            for pos in ['nouns', 'verbs', 'adjectives']:
                for word, count in top_pos[pos]:
                    POSTag.objects.create(
                        sentiment_analysis=sentiment_analysis,
                        pos=pos,
                        word=word,
                        count=count,
                    )

    print("Plotting sentiment distribution...")
    plot_sentiment_distribution(vader_scores, model_predictions)

    print("Creating word clouds...")

    # Keywords word cloud
    if keywords:
        create_word_cloud(dict(keywords), 'keywords')
    else:
        print("No keywords found. Skipping keywords word cloud.")

    # Named entities word cloud
    entity_dict = {entity[0]: count for (entity, count) in entities}
    if entity_dict:
        create_word_cloud(entity_dict, 'named_entities')
    else:
        print("No named entities found. Skipping named entities word cloud.")
    
    # POS word clouds
    for pos in ['nouns', 'verbs', 'adjectives']:
        pos_dict = dict(top_pos[pos])
        if pos_dict:
            create_word_cloud(pos_dict, f'{pos}_pos')
        else:
            print(f"No {pos} found. Skipping {pos} word cloud.")

    print("Analysis completed successfully.")

if __name__ == "__main__":
    analyze_sentiments()