import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def analyze_sentiment_scores(sentiments):
    scores = [s['sentiment_score'] for s in sentiments]
    mean_score = np.mean(scores)
    median_score = np.median(scores)
    mode_score = Counter(scores).most_common(1)[0][0]
    
    plt.hist(scores, bins=20)
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.title('Sentiment Score Distribution')
    plt.show()
    
    return {
        'mean': mean_score,
        'median': median_score,
        'mode': mode_score
    }
