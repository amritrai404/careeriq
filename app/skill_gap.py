"""
CareerIQ - Skill Gap Analyzer
-----------------------------
Prioritizes missing skills into Critical / Important / Nice to Have
based on:
    - Frequency in the job description
    - Skill category (soft skills = low priority)
"""

from app.skill_extractor import extract_skills_with_counts
from data.skills import get_category


# ---------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------
LOW_PRIORITY_CATEGORIES = {"Soft Skills"}

CRITICAL_THRESHOLD = 3     # appears >= 3 times -> Critical
IMPORTANT_THRESHOLD = 2    # appears >= 2 times -> Important
                           # else -> Nice to Have


def categorize_missing_skills(missing_skills, job_description):
    """
    Categorize missing skills by priority.

    Args:
        missing_skills (list[str]): Skills missing from resume.
        job_description (str): Raw JD text (for frequency analysis).

    Returns:
        dict: {
            "critical": list[str],
            "important": list[str],
            "nice_to_have": list[str],
        }
    """
    if not missing_skills:
        return {"critical": [], "important": [], "nice_to_have": []}

    # Get frequency counts from JD
    jd_counts = extract_skills_with_counts(job_description)

    critical = []
    important = []
    nice_to_have = []

    for skill in missing_skills:
        category = get_category(skill)
        frequency = jd_counts.get(skill, 1)

        # Soft skills never go to Critical
        if category in LOW_PRIORITY_CATEGORIES:
            nice_to_have.append(skill)
            continue

        if frequency >= CRITICAL_THRESHOLD:
            critical.append(skill)
        elif frequency >= IMPORTANT_THRESHOLD:
            important.append(skill)
        else:
            nice_to_have.append(skill)

    return {
        "critical": sorted(critical),
        "important": sorted(important),
        "nice_to_have": sorted(nice_to_have),
    }