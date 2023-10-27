from transformers import pipeline


nlp = pipeline("sentiment-analysis")

def scoring(text):
    results = nlp(text)
    for result in results:
        score = result['score']
        return score



# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# # Download the VADER lexicon if you haven't already
# nltk.download('vader_lexicon')

# # Initialize the VADER sentiment analyzer
# analyzer = SentimentIntensityAnalyzer()

# def analyze_sentiment(text):
#     sentiment_scores = analyzer.polarity_scores(text)
#     compound_score = sentiment_scores['compound']

#     if compound_score >= 0.05:
#         sentiment = "Positive"
#     elif compound_score <= -0.05:
#         sentiment = "Negative"
#     else:
#         sentiment = "Neutral"

#     return sentiment

# # Input text for sentiment analysis
# text = "I love this product. It's amazing!"

# # Perform sentiment analysis
# sentiment = analyze_sentiment(text)

# # Display the sentiment result
# print(f"Sentiment: {sentiment}")
