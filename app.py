import streamlit as st
from textblob import TextBlob
import pickle

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment
    return sentiment.polarity  # Value between -1 (negative) and +1 (positive)

# Positive language suggestions dictionary
suggestions = {
    "stupid": "thoughtful",
    "idiot": "inexperienced",
    "hate": "dislike",
    "shut up": "please be quiet"
}

# Suggest alternative phrasing
def suggest_alternative(text):
    words = text.lower().split()
    alternative_text = " ".join([suggestions.get(word, word) for word in words])
    return alternative_text

# Function for offensive language detection with sentiment
def detect_and_suggest_with_sentiment(text):
    # Predict if the text is offensive
    prediction = model.predict([text])[0]
    if prediction == 'offensive':
        severity_score = analyze_sentiment(text)
        if severity_score < -0.5:
            severity = "High - Strongly negative sentiment."
        elif severity_score < 0:
            severity = "Medium - Moderately negative sentiment."
        else:
            severity = "Low - Not strongly negative."
        suggestion = suggest_alternative(text)
        return prediction, severity, suggestion
    else:
        return "non-offensive", None, None

# Streamlit UI
st.title("Offensive Language Detection and Suggestion Tool")
st.write("Type a message to analyze for potential offensive content:")

# User input
user_input = st.text_input("Enter your message:")

# Analyze button
if st.button("Analyze"):
    if user_input:
        prediction, severity, suggestion = detect_and_suggest_with_sentiment(user_input)
        if prediction == "offensive":
            st.error("Detected offensive language!")
            st.write("Severity:", severity)
            st.write("Suggested positive alternative:", suggestion)
        else:
            st.success("This message is safe.")
    else:
        st.warning("Please enter a message.")
