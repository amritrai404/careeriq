"""
CareerIQ - Profile Matcher
--------------------------
Finds similar resume profiles using K-Means clustering
and TF-IDF cosine similarity.

Gracefully handles missing dataset (e.g., on Streamlit Cloud
where data/raw/resumes.csv is not pushed).
"""

import os
import joblib
import numpy as np
import pandas as pd

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

KMEANS_PATH = os.path.join(MODEL_DIR, "kmeans_profiles.pkl")
SVD_PATH = os.path.join(MODEL_DIR, "svd.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
DATA_PATH = os.path.join(DATA_DIR, "resumes.csv")

_cache = {
    "loaded": False,
    "available": False,
    "kmeans": None,
    "svd": None,
    "vectorizer": None,
    "df": None,
    "X": None,
}


def is_model_available():
    """Check if all needed artifacts exist (including dataset)."""
    return all(
        os.path.exists(p)
        for p in [KMEANS_PATH, SVD_PATH, VECTORIZER_PATH, DATA_PATH]
    )


def _load():
    """Load all needed artifacts (only once)."""
    if _cache["loaded"]:
        return

    _cache["loaded"] = True

    try:
        if not is_model_available():
            _cache["available"] = False
            return

        from sklearn.metrics.pairwise import cosine_similarity  # noqa

        _cache["kmeans"] = joblib.load(KMEANS_PATH)
        _cache["svd"] = joblib.load(SVD_PATH)
        _cache["vectorizer"] = joblib.load(VECTORIZER_PATH)
        _cache["df"] = pd.read_csv(DATA_PATH)

        X = _cache["vectorizer"].transform(
            _cache["df"]["Resume_str"].astype(str)
        )
        _cache["X"] = X
        _cache["available"] = True

    except Exception:
        _cache["available"] = False


def find_similar_profiles(user_text, top_n=5):
    """
    Find top N similar resumes from the dataset.

    Returns empty list if dataset is not available
    (e.g., on Streamlit Cloud).
    """
    if not user_text or not user_text.strip():
        return []

    _load()

    if not _cache["available"]:
        return []

    try:
        from sklearn.metrics.pairwise import cosine_similarity

        user_vec = _cache["vectorizer"].transform([user_text])
        sims = cosine_similarity(user_vec, _cache["X"])[0]
        top_idx = sims.argsort()[::-1][:top_n]

        results = []
        for idx in top_idx:
            results.append({
                "similarity": round(float(sims[idx]) * 100, 2),
                "category": str(_cache["df"].iloc[idx]["Category"]),
            })
        return results
    except Exception:
        return []