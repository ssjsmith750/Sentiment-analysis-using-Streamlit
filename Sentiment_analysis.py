import streamlit as st
from textblob import TextBlob

# Create a Streamlit app title
st.title("Social Media Sentiment Analysis")

# Create a text area for user input
user_input = st.text_area("Enter your social media text:")

# Define a function for sentiment analysis
def analyze_sentiment(text):
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"
    return sentiment_label, sentiment

# Add a button for sentiment analysis
if st.button("Analyze"):
    if user_input:
        sentiment_label, sentiment = analyze_sentiment(user_input)
        st.write(f"Sentiment: {sentiment_label}")
        st.write(f"Sentiment Score: {sentiment:.2f}")
        
        # Emoticon representation
        if sentiment_label == "Positive":
            st.write("😃")
        elif sentiment_label == "Negative":
            st.write("😞")
        else:
            st.write("😐")

        # Sentiment explanation
        if sentiment > 0:
            st.write("This text is generally positive.")
        elif sentiment < 0:
            st.write("This text is generally negative.")
        else:
            st.write("This text is neutral.")

    else:
        st.warning("Please enter some text to analyze.")


st.markdown("This simple app uses TextBlob to perform sentiment analysis on your social media text. It provides a sentiment label, score, emoticon, and explanation.")
