import string

def clean_text(text):
    # Remove punctuation and convert to lowercase
    text = ''.join([char.lower() for char in text if char not in string.punctuation])
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text