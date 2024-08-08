import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def perform_ner(texts):
    all_entities = []
    for text in texts:
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        all_entities.extend(entities)
    return all_entities
