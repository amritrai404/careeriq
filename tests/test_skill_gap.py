"""
Tests for app/skill_gap.py
"""

from app.skill_gap import categorize_missing_skills


def test_empty_missing():
    result = categorize_missing_skills([], "some jd")
    assert result["critical"] == []
    assert result["important"] == []
    assert result["nice_to_have"] == []


def test_soft_skill_goes_to_nice():
    jd = "Communication Communication Communication"
    result = categorize_missing_skills(["Communication"], jd)
    assert "Communication" in result["nice_to_have"]


def test_critical_skill():
    jd = "AWS AWS AWS needed"
    result = categorize_missing_skills(["AWS"], jd)
    assert "AWS" in result["critical"]


def test_important_skill():
    jd = "Docker Docker required"
    result = categorize_missing_skills(["Docker"], jd)
    assert "Docker" in result["important"]


def test_nice_to_have_skill():
    jd = "FastAPI is a plus"
    result = categorize_missing_skills(["FastAPI"], jd)
    assert "FastAPI" in result["nice_to_have"]