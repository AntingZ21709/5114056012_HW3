import streamlit as st
import joblib
import re
import string
from PIL import Image

# Load the trained model and vectorizer
model = joblib.load('models/spam_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

def clean_text(text):
    """
    Applies text cleaning to the input text.
    """
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\d+', '', text)
    text = ' '.join(text.split())
    return text

# Streamlit app
st.title("Spam Message Classifier")

st.write("Enter a message to check if it's spam or not.")

# User input
message = st.text_area("Message")

if st.button("Check"):
    if message:
        # Clean the input message
        cleaned_message = clean_text(message)

        # Vectorize the message
        vectorized_message = vectorizer.transform([cleaned_message])

        # Make prediction
        prediction = model.predict(vectorized_message)[0]
        prediction_proba = model.predict_proba(vectorized_message)[0]

        # Display the result
        st.subheader("Result")
        if prediction == 'spam':
            st.error("This message is classified as SPAM.")
        else:
            st.success("This message is classified as NOT SPAM (ham).")

        # Display confidence score
        st.subheader("Confidence Score")
        st.write(f"**Spam:** {prediction_proba[1]:.4f}")
        st.write(f"**Not Spam (Ham):** {prediction_proba[0]:.4f}")
    else:
        st.warning("Please enter a message to check.")

# Overall Model Performance
st.title("Overall Model Performance")

st.write("The following charts show the performance of the Logistic Regression model on the test set.")

# Display images
image_cm = Image.open('confusion_matrix.png')
st.image(image_cm, caption='Confusion Matrix')

image_pm = Image.open('performance_metrics.png')
st.image(image_pm, caption='Performance Metrics')