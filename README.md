# HarmonyBot Project Documentation

## Project Overview
**HarmonyBot** is an AI-powered tool developed to detect and mitigate offensive language in real time, aiming to create safer online spaces, particularly for vulnerable groups such as women and girls. The bot leverages machine learning, sentiment analysis, and Google’s Perspective API to identify toxic language, assess its severity, and suggest positive alternatives, fostering a more respectful digital environment.

---

## Table of Contents
1. [Inspiration](#inspiration)
2. [What HarmonyBot Does](#what-harmonybot-does)
3. [Technologies Used](#technologies-used)
4. [System Architecture](#system-architecture)
5. [How It Works](#how-it-works)
6. [Challenges and Solutions](#challenges-and-solutions)
7. [Accomplishments](#accomplishments)
8. [Future Enhancements](#future-enhancements)
9. [How to Test](#how-to-test)
10. [Contribution Towards Gender Equality](#contribution-towards-gender-equality)

---

## Inspiration
The idea for HarmonyBot stemmed from the need to address the high prevalence of online harassment, especially targeting women and girls. The project aims to foster safer digital spaces by mitigating abusive language, empowering users to engage confidently without fear of harassment.

---

## What HarmonyBot Does
HarmonyBot analyzes messages and offers a detailed analysis that includes:
- **Offensive Language Detection**: Classifies content as “offensive” or “non-offensive” using a machine learning model.
- **Sentiment Analysis**: Assesses emotional tone to determine the negativity of the content.
- **Toxicity Scoring**: Uses the Google Perspective API to quantify the message’s toxicity.
- **Positive Alternatives**: Suggests respectful alternatives for flagged language to encourage positive communication.
- **Real-Time Feedback**: Provides instant insights on the offensive content, severity, toxicity, and alternatives to the user.

---

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Streamlit (for UI)
- **Machine Learning**: Pre-trained model with TextBlob for sentiment analysis
- **API Integration**: Google Perspective API for toxicity analysis
- **Environment Management**: dotenv (to manage API keys securely)
- **Libraries**: TextBlob, Pickle, os, requests, subprocess

---

## System Architecture
The HarmonyBot architecture includes:
- **Frontend**: Streamlit UI for user input, feedback display, and results visualization.
- **Backend**:
   - **Model**: Machine learning model trained to classify offensive content.
   - **Sentiment Analyzer**: TextBlob to evaluate message sentiment.
   - **Toxicity API**: Google Perspective API for toxicity scoring.
- **Database**: Not applicable in the current version, as data is not stored.

---

## How It Works
1. **User Input**: Users enter a message in the Streamlit UI.
2. **Offensive Language Detection**: The pre-trained model classifies the message as “offensive” or “non-offensive.”
3. **Sentiment Analysis**: TextBlob assesses the emotional tone of the message.
4. **Toxicity Scoring**: Google Perspective API provides a toxicity score for further evaluation.
5. **Suggestions**: Offensive words are replaced with respectful alternatives.
6. **Feedback**: Results on offensiveness, sentiment, severity, toxicity score, and suggested alternatives are displayed to the user.

---

## Challenges and Solutions
- **Perspective API Integration**: Managing API responses and ensuring accuracy required careful setup.
- **Data Sensitivity**: Handled API keys securely with environment variables and dotenv.
- **False Positives**: Fine-tuned the model to better identify true offensive content and minimize false positives.

---

## Accomplishments
- Successfully integrated offensive language detection with toxicity and sentiment analysis.
- Created a real-time, interactive UI for instant feedback on language use.
- Developed a dictionary for respectful alternatives, promoting positive communication.

---

## Future Enhancements
1. **Multilingual Support**: Expand offensive language detection across multiple languages.
2. **Advanced Sentiment Analysis**: Use a more sophisticated model to assess nuanced contexts.
3. **Live Chat Monitoring**: Enable real-time chat monitoring and automated warnings.
4. **User Customization**: Allow users to adjust sensitivity levels for personal preference.
5. **Browser Extension**: Develop a browser extension for real-time content filtering.
6. **Bias Testing**: Continuously test and adjust the model for biases and fairness.

---

## How to Test
1. **Launch HarmonyBot**: Open the Streamlit app or run locally.
2. **Enter Test Sentences**:
   - Test with both offensive and non-offensive sentences.
   - Check for sentiment accuracy with positive, neutral, and negative tones.
   - Confirm toxicity scores with varying levels of abusive language.
   - Observe the alternatives suggested for flagged language.
3. **Analyze Results**: Verify that flagged messages, sentiment, toxicity scores, and suggested phrases align with expectations.

---

## Contribution Towards Gender Equality
HarmonyBot is designed to combat online harassment, which disproportionately impacts women and girls. By filtering harmful language and encouraging positive alternatives, it fosters a safer online environment that promotes gender equality. HarmonyBot empowers women to participate freely in digital spaces and provides data insights to support gender-sensitive policies.

---
