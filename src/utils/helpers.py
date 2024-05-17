def clean_text(text):
    import re
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = re.sub(r'\d', '', text)  # Remove digits
    return text.lower()

def tokenize_text(text):
    import nltk
    from nltk.tokenize import word_tokenize
    nltk.download('punkt')
    tokens = word_tokenize(text)
    return tokens

def remove_stopwords(tokens, language='english'):
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words(language))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

def lemmatize_tokens(tokens):
    import nltk
    from nltk.stem import WordNetLemmatizer
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens
