from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

def detect_emotions(texts):
    all_scores = []
    for text in texts:
        sentiment = analyzer.polarity_scores(text)
        all_scores.append(sentiment['compound'])
    return all_scores
