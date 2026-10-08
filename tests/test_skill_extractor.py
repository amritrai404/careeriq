"""
Tests for app/skill_extractor.py
"""

from app.skill_extractor import extract_skills, extract_skills_with_counts


def test_extract_basic_skills():
    text = "Python developer with SQL and Pandas experience."
    skills = extract_skills(text)
    assert "Python" in skills
    assert "SQL" in skills
    assert "Pandas" in skills


def test_case_insensitive_matching():
    text = "python, SQL, PANDAS"
    skills = extract_skills(text)
    assert "Python" in skills
    assert "SQL" in skills
    assert "Pandas" in skills


def test_alias_matching():
    text = "Used ml and sklearn for modeling."
    skills = extract_skills(text)
    assert "Machine Learning" in skills
    assert "Scikit-learn" in skills


def test_duplicate_removal():
    text = "Python Python Python SQL SQL"
    skills = extract_skills(text)
    assert skills.count("Python") == 1
    assert skills.count("SQL") == 1


def test_empty_text():
    assert extract_skills("") == []
    assert extract_skills("   ") == []
    assert extract_skills(None) == []


def test_word_boundary():
    """
    'R' should not match inside 'React'.
    """
    text = "I use React for frontend."
    skills = extract_skills(text)
    assert "R" not in skills
    assert "React" in skills


def test_counts():
    text = "AWS AWS Docker AWS"
    counts = extract_skills_with_counts(text)
    assert counts["AWS"] == 3
    assert counts["Docker"] == 1