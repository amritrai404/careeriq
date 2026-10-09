"""
CareerIQ - Role Predictor
-------------------------
Predicts suitable job roles from resume text using a
trained Random Forest classifier + TF-IDF vectorizer.
"""

import os
import joblib

# Model paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "role_classifier.pkl")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")

# Lazy loading (sirf jab zaroorat ho tab load karo)
_model = None
_vectorizer = None


def _load_model():
    """Load model + vectorizer (cached)."""
    global _model, _vectorizer

    if _model is None or _vectorizer is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model not found: {MODEL_PATH}. "
                "Please train the model first (notebook 03)."
            )
        if not os.path.exists(VECTORIZER_PATH):
            raise FileNotFoundError(
                f"Vectorizer not found: {VECTORIZER_PATH}. "
                "Please train the model first (notebook 03)."
            )
        _model = joblib.load(MODEL_PATH)
        _vectorizer = joblib.load(VECTORIZER_PATH)

    return _model, _vectorizer


def predict_roles(resume_text, top_n=3):
    """
    Predict top N suitable roles from resume text.

    Args:
        resume_text (str): Full resume text.
        top_n (int): Number of top predictions to return.

    Returns:
        list[dict]: [{"role": str, "confidence": float}, ...]
    """
    if not resume_text or not resume_text.strip():
        return []

    model, vectorizer = _load_model()

    # Transform text
    X = vectorizer.transform([resume_text])

    # Predict probabilities
    probs = model.predict_proba(X)[0]
    top_idx = probs.argsort()[::-1][:top_n]

    results = []
    for i in top_idx:
        results.append({
            "role": str(model.classes_[i]),
            "confidence": round(float(probs[i]) * 100, 2),
        })

    return results


def is_model_available():
    """Check if trained model files exist."""
    return (
        os.path.exists(MODEL_PATH) and
        os.path.exists(VECTORIZER_PATH)
    )