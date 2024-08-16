from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def detect_emotions(reviews):
    analyzer = SentimentIntensityAnalyzer()
    scores = []
    for review in reviews:
        score = analyzer.polarity_scores(review)['compound']
        scores.append(score)
    return scores