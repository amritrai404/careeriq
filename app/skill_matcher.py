"""
CareerIQ - Skill Matcher
------------------------
Compares resume skills against job description skills
and produces matched skills, missing skills, match score,
and a human-readable match status.
"""


# ---------------------------------------------------------------
# Match Status Thresholds
# ---------------------------------------------------------------
STRONG_THRESHOLD = 75      # >= 75% -> Strong Match
MODERATE_THRESHOLD = 50    # >= 50% -> Moderate Match
                           # < 50%  -> Needs Improvement


def get_match_status(score):
    """
    Convert a numeric match score into a human-readable status.

    Args:
        score (float): Match score (0-100).

    Returns:
        str: Status label with emoji.
    """
    if score >= STRONG_THRESHOLD:
        return "🟢 Strong Match"
    elif score >= MODERATE_THRESHOLD:
        return "🟡 Moderate Match"
    else:
        return "🔴 Needs Improvement"


def match_skills(resume_skills, required_skills):
    """
    Compare resume skills against required (JD) skills.

    Args:
        resume_skills (list[str]): Skills extracted from resume.
        required_skills (list[str]): Skills extracted from job description.

    Returns:
        dict: {
            "matched": list[str],
            "missing": list[str],
            "extra": list[str],       # skills in resume but not required
            "match_score": float,     # 0-100
            "status": str,
            "total_required": int,
            "total_matched": int,
        }
    """
    resume_set = set(resume_skills or [])
    required_set = set(required_skills or [])

    matched = sorted(resume_set & required_set)
    missing = sorted(required_set - resume_set)
    extra = sorted(resume_set - required_set)

    total_required = len(required_set)
    total_matched = len(matched)

    if total_required == 0:
        match_score = 0.0
    else:
        match_score = round((total_matched / total_required) * 100, 2)

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra,
        "match_score": match_score,
        "status": get_match_status(match_score),
        "total_required": total_required,
        "total_matched": total_matched,
    }