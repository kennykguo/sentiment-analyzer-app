import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_sentiment_distribution(vader_scores, model_scores, save_path=None):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(vader_scores, bins=20, edgecolor='black')
    plt.title('VADER Sentiment Score Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    model_scores_numeric = [1 if score == 'positive' else 0 for score in model_scores]
    plt.hist(model_scores_numeric, bins=2, edgecolor='black')
    plt.title('Model Sentiment Score Distribution')
    plt.xlabel('Sentiment (0: Negative, 1: Positive)')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def create_word_cloud(word_freq, title, save_path=None):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
        return wordcloud
    else:
        plt.show()
        return wordcloud