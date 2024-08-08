from rake_nltk import Rake

# Initialize Rake
rake = Rake()

def extract_keywords(texts):
    all_keywords = []
    for text in texts:
        rake.extract_keywords_from_text(text)
        keywords = rake.get_ranked_phrases()
        all_keywords.extend(keywords)
    return all_keywords
