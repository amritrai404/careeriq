"""
CareerIQ - Skill Extractor
--------------------------
Extracts known skills from raw text (resume or job description)
using the CareerIQ skill database.
"""

import re

from data.skills import (
    get_all_skills,
    SKILL_ALIASES,
)


# ---------------------------------------------------------------
# Pre-compiled matchers (built once at import for speed)
# ---------------------------------------------------------------
# Sort by length descending so "Machine Learning" matches before "Learning"
_ALL_SKILLS = sorted(get_all_skills(), key=len, reverse=True)


def _build_skill_pattern(skill):
    """
    Build a regex pattern for a single skill.

    Uses word boundaries so 'R' doesn't match inside 'React',
    and 'C' doesn't match inside 'CSS'.
    """
    escaped = re.escape(skill)
    return re.compile(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", re.IGNORECASE)


_SKILL_PATTERNS = [(skill, _build_skill_pattern(skill)) for skill in _ALL_SKILLS]


# ---------------------------------------------------------------
# Core Extraction
# ---------------------------------------------------------------
def extract_skills(text):
    """
    Extract known skills from a block of text.

    Args:
        text (str): Resume or job description text.

    Returns:
        list[str]: Sorted list of unique canonical skills found.
    """
    if not text or not text.strip():
        return []

    detected = set()

    # 1. Match canonical skills
    for skill, pattern in _SKILL_PATTERNS:
        if pattern.search(text):
            detected.add(skill)

    # 2. Match aliases (case-insensitive)
    lowered = text.lower()
    for alias, canonical in SKILL_ALIASES.items():
        # Use word boundaries via regex for aliases too
        alias_pattern = re.compile(
            rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])",
            re.IGNORECASE,
        )
        if alias_pattern.search(lowered):
            detected.add(canonical)

    return sorted(detected)


def extract_skills_with_counts(text):
    """
    Same as extract_skills but also returns how many times
    each skill appears in the text (useful for skill-gap priority later).

    Args:
        text (str): Resume or job description text.

    Returns:
        dict[str, int]: {skill_name: frequency}
    """
    if not text or not text.strip():
        return {}

    counts = {}

    # Canonical skills
    for skill, pattern in _SKILL_PATTERNS:
        matches = pattern.findall(text)
        if matches:
            counts[skill] = counts.get(skill, 0) + len(matches)

    # Aliases
    for alias, canonical in SKILL_ALIASES.items():
        alias_pattern = re.compile(
            rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])",
            re.IGNORECASE,
        )
        matches = alias_pattern.findall(text)
        if matches:
            counts[canonical] = counts.get(canonical, 0) + len(matches)

    return counts