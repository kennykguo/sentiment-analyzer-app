import pandas as pd
import torch
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.text_cleaning import clean_text
from modules.ner import perform_ner
from modules.pos_tagging import get_pos_tags, top_nouns_verbs_adjectives
from modules.emotion_detection import detect_emotions
from modules.keyword_extraction import extract_keywords
from modules.plot_distribution import analyze_sentiment_scores, plot_sentiment_distribution, average_word_count
from pytorch_model.transformer import Transformer, text_transform, vocab

def predict_single_text(model, text, text_transform, vocab):
    device = next(model.parameters()).device
    tokens = text_transform([text]).to(device)
    
    with torch.no_grad():
        logits, attn_weights = model(tokens)
    
    probs = torch.nn.functional.softmax(logits, dim=-1)
    label = torch.argmax(probs, dim=1)
    
    # Analyze attention weights
    att_map = attn_weights[0, -1, :, :]  # Last head, first sample
    att_weights = att_map[0]  # Attention weights for the [CLS] token
    top10 = att_weights.argsort(descending=True)[:10]
    top10_tokens = [vocab.lookup_token(tokens[0][idx].item()) for idx in top10]
    
    prediction = 'positive' if label.item() == 1 else 'negative'
    return prediction, top10_tokens

def import_and_process_data(file_path):
    df = pd.read_excel(file_path, header=None, names=['review'])
    reviews = df['review'].tolist()
    

    
    # Clean the entire list of reviews
    cleaned_reviews = [clean_text(review) for review in reviews]
    


    # NER
    entities = perform_ner(cleaned_reviews)
    


    # POS Tagging
    pos_tags = get_pos_tags(cleaned_reviews)
    top_pos_tags = top_nouns_verbs_adjectives(pos_tags)
    


    # Emotion Detection
    sentiment_scores = detect_emotions(cleaned_reviews)
    


    # Keyword Extraction
    keywords = extract_keywords(cleaned_reviews)
    


    # Compute statistics
    avg_sentiment_score = analyze_sentiment_scores(sentiment_scores)
    avg_word_count = average_word_count(reviews)
    print(f"Average Sentiment Score: {avg_sentiment_score}")
    print(f"Average Word Count per Review: {avg_word_count}")
    


    # NER
    print("\nNER:")
    print(set(entities))  # Print unique entities



    # POS
    print("\nTop POS Tags:")
    print('Nouns:')
    print(top_pos_tags['nouns'])
    print('Verbs:')
    print(top_pos_tags['verbs'])
    print('Adj:')
    print(top_pos_tags['adjectives'])



    # Keyword extraction
    print("\nKeywords Extracted:")
    print(set(keywords))  # Print unique keywords
    


    # Plot sentiment distribution
    plot_sentiment_distribution(sentiment_scores)



    # PyTorch Model Inference
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = Transformer()
    model.load_state_dict(torch.load('model_weights/gpt.pth'))
    model = model.to(device)
    model.eval()
    print("\nPyTorch Model Predictions:")
    for i, review in enumerate(cleaned_reviews):
        prediction, top_words = predict_single_text(model, review, text_transform, vocab)
        print(f"Review {i+1} - Prediction: {prediction}")
        print(f"Top words influencing the prediction: {', '.join(top_words)}")
        print()



# Define the file path
file_path = 'sentiment_data/73.xlsx'

import_and_process_data(file_path)