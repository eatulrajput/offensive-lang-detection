import streamlit as st
from textblob import TextBlob
import pickle
import requests
from dotenv import load_dotenv
import os
import subprocess

import streamlit as st

# Set the page title and icon (optional)
st.set_page_config(page_title="HarmonBot", page_icon="HarmonyBot.png")


# Load environment variables from the .env file
load_dotenv()

# Load the Perspective API key from Streamlit secrets
api_key = st.secrets["PERSPECTIVE_API_KEY"]

# Get the Perspective API key from environment variable
api_key = os.getenv('PERSPECTIVE_API_KEY')

# Load GitHub credentials from secrets
github_username = st.secrets["GITHUB_USERNAME"]
github_token = st.secrets["GITHUB_TOKEN"]

# Update repository URL with username and token
repo_url = f"https://{github_username}:{github_token}@github.com/eatulrajput/offensive-lang-detection.git"

# # Pull changes using subprocess with credentials
# try:
#     subprocess.run(["git", "pull", repo_url], check=True)
#     st.success("App updated successfully from GitHub!")
# except subprocess.CalledProcessError:
#     st.error("Failed to update app files from GitHub.")




# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = TextBlob(text).sentiment
    return sentiment.polarity  # Value between -1 (negative) and +1 (positive)

# Enhanced Positive language suggestions dictionary
suggestions = {
    "stupid": "thoughtful",
    "idiot": "inexperienced",
    "hate": "dislike",
    "shut up": "please be quiet",
    "shit": "rubbish",
    "dumb": "uninformed",
    "moron": "novice",
    "loser": "underdog",
    "ugly": "unattractive",
    "fuck": "freak"
}

# Suggest alternative phrasing
def suggest_alternative(text):
    words = text.lower().split()
    alternative_text = " ".join([suggestions.get(word, word) for word in words])
    return alternative_text

# Function to get toxicity score from Perspective API
def get_toxicity_score(text, api_key):
    url = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze'
    data = {
        'comment': {'text': text},
        'requestedAttributes': {'TOXICITY': {}}
    }
    
    # Make the request
    response = requests.post(url, params={'key': api_key}, json=data)
    
    # Check if response is valid
    if response.status_code == 200:
        result = response.json()
        if 'attributeScores' in result and 'TOXICITY' in result['attributeScores']:
            toxicity_score = result['attributeScores']['TOXICITY']['summaryScore']['value']
            toxicity_percentage = toxicity_score * 100  # Convert to percentage
            return toxicity_percentage
        else:
            print("Error: No toxicity score found.")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function for offensive language detection with sentiment and toxicity score
def detect_and_suggest_with_sentiment(text, api_key):
    # Predict if the text is offensive
    prediction = model.predict([text])[0]
    
    # Get toxicity score from Perspective API
    toxicity_percentage = get_toxicity_score(text, api_key)
    
    # Sentiment analysis
    severity_score = analyze_sentiment(text)
    if prediction == 'offensive' or (toxicity_percentage and toxicity_percentage > 50):
        if severity_score < -0.5:
            severity = "High - Strongly negative sentiment."
        elif severity_score < 0:
            severity = "Medium - Moderately negative sentiment."
        else:
            severity = "Low - Not strongly negative."
        
        # Suggest alternative phrasing based on detected toxicity and offense
        suggestion = suggest_alternative(text)
        return prediction, severity, suggestion, toxicity_percentage
    else:
        return "non-offensive", None, None, toxicity_percentage

# Streamlit UI
# Create two columns
col1, col2 = st.columns([1, 5])  # Adjust the ratio as needed

with col1:
    # Display the image in the first column
    st.image("HarmonyBot.png", width=500)  # Adjust width as needed

with col2:
    # Display the title in the second column
    st.title("HarmonyBot")
st.write("An Offensive Language Detection and Suggestion Tool")
st.write("Type a message to analyze for potential offensive content:")

# User input
user_input = st.text_input("Enter your message:")

# Analyze button
if st.button("Analyze"):
    if user_input:
        prediction, severity, suggestion, toxicity_percentage = detect_and_suggest_with_sentiment(user_input, api_key)
        if prediction == "offensive":
            st.error("Detected offensive language!")
            st.write("Severity:", severity)
            st.write("Suggested positive alternative:", suggestion)
            st.write(f"Toxicity score: {toxicity_percentage:.2f}%")
        else:
            st.success("This message is safe.")
            st.write(f"Toxicity score: {toxicity_percentage:.2f}%" if toxicity_percentage is not None else "Toxicity score not available.")
    else:
        st.warning("Please enter a message.")
