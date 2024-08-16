from rake_nltk import Rake
from collections import Counter

rake = Rake()

def extract_keywords(texts, num_keywords):
    all_keywords = []
    for text in texts:
        rake.extract_keywords_from_text(text)
        keywords = rake.get_ranked_phrases()
        all_keywords.extend(keywords)
    return Counter(all_keywords).most_common(num_keywords)