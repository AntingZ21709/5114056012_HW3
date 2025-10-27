import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

def clean_text(text):
    """
    Applies text cleaning to the input text.
    """
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\d+', '', text)
    text = ' '.join(text.split())
    return text

def preprocess_data(filepath):
    """
    Loads data, preprocesses the text, and creates TF-IDF features.
    Saves the vectorizer for future use.
    """
    df = pd.read_csv(filepath, names=['label', 'message'])
    df['cleaned_message'] = df['message'].apply(clean_text)
    
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(df['cleaned_message'])
    y = df['label']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Save the vectorizer and the split data
    joblib.dump(vectorizer, 'models/vectorizer.pkl')
    joblib.dump((X_train, X_test, y_train, y_test), 'data/processed_data.pkl')

    return X_train, X_test, y_train, y_test, vectorizer

if __name__ == '__main__':
    # This block will run if the script is executed directly
    # Example usage:
    X_train, X_test, y_train, y_test, vectorizer = preprocess_data('data/sms_spam_no_header.csv')
    print("Data preprocessed successfully.")
    print("Shape of X_train:", X_train.shape)
    print("Shape of X_test:", X_test.shape)
    print("y_train distribution:\n", y_train.value_counts())
    print("y_test distribution:\n", y_test.value_counts())