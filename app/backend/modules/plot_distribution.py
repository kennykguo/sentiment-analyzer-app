import numpy as np
import matplotlib.pyplot as plt

def analyze_sentiment_scores(scores):
    mean_score = np.mean(scores)
    return mean_score

def plot_sentiment_distribution(scores):
    plt.figure(figsize=(10, 6))
    plt.hist(scores, bins=20, edgecolor='black')
    plt.title('Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def average_word_count(texts):
    word_counts = [len(text.split()) for text in texts]
    return np.mean(word_counts)
