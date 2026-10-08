"""
Tests for app/skill_matcher.py
"""

from app.skill_matcher import match_skills, get_match_status


def test_basic_match():
    resume = ["Python", "SQL", "Pandas"]
    required = ["Python", "SQL", "Pandas", "AWS", "Docker"]
    result = match_skills(resume, required)

    assert result["total_matched"] == 3
    assert result["total_required"] == 5
    assert result["match_score"] == 60.0
    assert "Pandas" in result["matched"]
    assert "AWS" in result["missing"]
    assert "Docker" in result["missing"]


def test_no_required_skills():
    result = match_skills(["Python"], [])
    assert result["match_score"] == 0.0
    assert result["missing"] == []


def test_perfect_match():
    resume = ["Python", "SQL"]
    required = ["Python", "SQL"]
    result = match_skills(resume, required)
    assert result["match_score"] == 100.0


def test_extra_skills():
    resume = ["Python", "SQL", "Rust"]
    required = ["Python", "SQL"]
    result = match_skills(resume, required)
    assert "Rust" in result["extra"]


def test_empty_inputs():
    result = match_skills([], [])
    assert result["match_score"] == 0.0
    assert result["matched"] == []
    assert result["missing"] == []


def test_get_match_status():
    assert "Strong" in get_match_status(80)
    assert "Moderate" in get_match_status(60)
    assert "Needs Improvement" in get_match_status(30)