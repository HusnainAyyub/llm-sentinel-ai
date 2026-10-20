"""Scikit-learn text classifier for prompt categories.

Trains a small TF-IDF + Logistic Regression model on the starter
dataset in data/prompts_starter_v1.csv (32 team written rows).
The dataset grows toward the 2,000 prompt target in data/README.md.
"""
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "prompts_starter_v1.csv")

_model = None

def get_model():
    global _model
    if _model is None:
        df = pd.read_csv(DATA_PATH)
        df = df.dropna(subset=["prompt_text", "category"])
        _model = Pipeline([
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
            ("clf", LogisticRegression(max_iter=1000)),
        ])
        _model.fit(df["prompt_text"], df["category"])
    return _model

def predict(prompt: str) -> str:
    return str(get_model().predict([prompt])[0])
