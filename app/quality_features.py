"""
CareerIQ - Quality Feature Extraction
-------------------------------------
Extracts hand-crafted features from resume text
for the resume quality score regressor.
"""

import re

from app.skill_extractor import extract_skills


# Action verbs commonly found in strong resumes
ACTION_VERBS = {
    "built", "designed", "developed", "created", "implemented",
    "optimized", "improved", "increased", "reduced", "led",
    "managed", "delivered", "deployed", "launched", "architected",
    "automated", "streamlined", "collaborated", "mentored", "trained",
    "achieved", "exceeded", "spearheaded", "initiated", "resolved",
}

# Common resume sections
SECTIONS = {
    "experience", "education", "skills", "projects", "certifications",
    "summary", "objective", "achievements", "awards", "publications",
    "languages", "interests", "volunteer",
}


def extract_quality_features(text):
    """
    Extract numerical features from resume text.

    Args:
        text (str): Resume text.

    Returns:
        list[float]: Feature vector.
    """
    if not text or not text.strip():
        return [0.0] * 8

    text_lower = text.lower()
    words = re.findall(r"\b[a-zA-Z]+\b", text_lower)

    # 1. Word count
    word_count = len(words)

    # 2. Unique word ratio (vocabulary richness)
    unique_ratio = len(set(words)) / max(word_count, 1)

    # 3. Skill count
    skill_count = len(extract_skills(text))

    # 4. Action verb count
    action_verb_count = sum(1 for w in words if w in ACTION_VERBS)

    # 5. Numbers / metrics mentions
    number_count = len(re.findall(r"\b\d+(?:\.\d+)?%?\b", text))

    # 6. Section count
    section_count = sum(1 for s in SECTIONS if s in text_lower)

    # 7. Average word length
    avg_word_len = (
        sum(len(w) for w in words) / max(word_count, 1)
    )

    # 8. Capitalized words (proper nouns / job titles)
    capitalized = len(re.findall(r"\b[A-Z][a-z]+\b", text))
    capitalized_ratio = capitalized / max(word_count, 1)

    return [
        float(word_count),
        float(unique_ratio),
        float(skill_count),
        float(action_verb_count),
        float(number_count),
        float(section_count),
        float(avg_word_len),
        float(capitalized_ratio),
    ]


FEATURE_NAMES = [
    "word_count",
    "unique_word_ratio",
    "skill_count",
    "action_verb_count",
    "number_count",
    "section_count",
    "avg_word_length",
    "capitalized_ratio",
]