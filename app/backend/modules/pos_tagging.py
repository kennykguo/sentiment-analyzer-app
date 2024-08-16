import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

def get_pos_tags(texts):
    all_tags = []
    for text in texts:
        doc = nlp(text)
        tags = [(token.text, token.pos_) for token in doc if not token.is_stop and token.is_alpha]
        all_tags.extend(tags)
    return all_tags

def top_pos_tags(tags, top_n=20):
    nouns = [word.lower() for word, pos in tags if pos == 'NOUN']
    verbs = [word.lower() for word, pos in tags if pos == 'VERB']
    adjectives = [word.lower() for word, pos in tags if pos == 'ADJ']
    
    return {
        'nouns': Counter(nouns).most_common(top_n),
        'verbs': Counter(verbs).most_common(top_n),
        'adjectives': Counter(adjectives).most_common(top_n)
    }