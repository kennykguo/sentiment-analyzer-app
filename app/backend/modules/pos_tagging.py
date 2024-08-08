def get_pos_tags(texts):
    all_tags = []
    for text in texts:
        tokens = word_tokenize(text)
        tags = pos_tag(tokens)
        all_tags.extend(tags)
    return all_tags


def top_nouns_verbs_adjectives(tags, top_n=10):
    nouns = [word for word, pos in tags if pos in ['NN', 'NNS', 'NNP', 'NNPS']]
    verbs = [word for word, pos in tags if pos.startswith('VB')]
    adjectives = [word for word, pos in tags if pos in ['JJ', 'JJR', 'JJS']]
    
    return {
        'nouns': nltk.FreqDist(nouns).most_common(top_n),
        'verbs': nltk.FreqDist(verbs).most_common(top_n),
        'adjectives': nltk.FreqDist(adjectives).most_common(top_n)
    }
