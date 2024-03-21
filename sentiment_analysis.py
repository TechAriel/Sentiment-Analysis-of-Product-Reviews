#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Import necessary libraries
import pandas as pd
import spacy
from textblob import TextBlob

#Load the Dataset
file_path = "amazon_product_reviews.csv"  # Update this path
dataframe = pd.read_csv(file_path)


# In[6]:


# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

# Preprocess the Text Data
# Function to preprocess text: remove stop words, punctuation, numbers, and perform lemmatization
def preprocess_text(text):
    doc = nlp(text)
    clean_text = ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct and not token.like_num])
    return clean_text

dataframe['cleaned_text'] = dataframe['reviews.text'].dropna().apply(preprocess_text)


# In[10]:


def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Apply sentiment analysis on the cleaned text
dataframe['sentiment_polarity'] = dataframe['cleaned_text'].apply(analyze_sentiment)
dataframe['sentiment'] = dataframe['sentiment_polarity'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral')

# Print results for the first 5 reviews
for index, row in dataframe.head(5).iterrows():
    print(f"Original Review: {row['reviews.text']}")
    print(f"Cleaned Text: {row['cleaned_text']}")
    print(f"Sentiment Polarity: {row['sentiment_polarity']}")
    print(f"Sentiment: {row['sentiment']}\n")


# In[8]:


# Compare Similarity of Two Reviews
# Function to compare the similarity between two pieces of text
def compare_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)

# Compute and print the similarity score between the two selected reviews
similarity_score = compare_similarity(dataframe['cleaned_text'].iloc[0], dataframe['cleaned_text'].iloc[1])
print(f'Similarity between two reviews: {similarity_score}')


# In[ ]:




