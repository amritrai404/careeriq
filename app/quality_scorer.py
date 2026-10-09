"""
CareerIQ - Quality Scorer
-------------------------
Predicts a resume quality score (0-100) using a trained
Gradient Boosting regressor.
"""

import os
import joblib

from app.quality_features import extract_quality_features


MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "quality_regressor.pkl")

_model = None


def _load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Quality model not found: {MODEL_PATH}"
            )
        _model = joblib.load(MODEL_PATH)
    return _model


def predict_quality(resume_text):
    """
    Predict a quality score for a resume.

    Args:
        resume_text (str): Full resume text.

    Returns:
        dict: {"score": float, "features": dict}
    """
    if not resume_text or not resume_text.strip():
        return {"score": 0.0, "features": {}}

    model = _load_model()
    features = extract_quality_features(resume_text)
    score = float(model.predict([features])[0])

    return {
        "score": round(max(0.0, min(score, 100.0)), 1),
        "features": features,
    }


def is_model_available():
    return os.path.exists(MODEL_PATH)