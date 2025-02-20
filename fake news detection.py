# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AH12ubc6Fy0NKCyoC-vECBPkkYhIPX4M
"""

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import fetch_20newsgroups

# Load Dataset (Using 20 Newsgroups dataset as an alternative)
categories = ['sci.space', 'talk.politics.mideast']  # Two categories as Fake & Real news example
newsgroups = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'))

# Convert to DataFrame
df = pd.DataFrame({'text': newsgroups.data, 'label': newsgroups.target})

# Map labels to binary values (0: Fake, 1: Real) - Assuming 'sci.space' as real and 'talk.politics.mideast' as fake
df['label'] = df['label'].map({0: 1, 1: 0})  # 1 for sci.space (real), 0 for politics.mideast (fake)

# Extract Features and Labels
X = df['text']
y = df['label']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert Text to Numerical Features
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Predictions & Evaluation
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)

# Print Results
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))