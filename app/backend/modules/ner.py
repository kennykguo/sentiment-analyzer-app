import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

def perform_ner(texts, num_entities):
    all_entities = []
    for text in texts:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        all_entities.extend(entities)
    return Counter(all_entities).most_common(num_entities)