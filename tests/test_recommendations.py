"""
Tests for app/recommendations.py
"""

from app.recommendations import (
    get_learning_suggestions,
    get_project_ideas,
    get_resume_tips,
)


def test_learning_suggestions_for_known_skill():
    suggestions = get_learning_suggestions(["AWS"])
    assert len(suggestions) == 1
    assert suggestions[0]["skill"] == "AWS"
    assert suggestions[0]["category"] == "Cloud & DevOps"
    assert "AWS" in suggestions[0]["suggestion"]


def test_learning_suggestions_for_unknown_skill():
    suggestions = get_learning_suggestions(["SomeUnknownSkill"])
    assert len(suggestions) == 1
    assert "SomeUnknownSkill" in suggestions[0]["suggestion"]


def test_project_ideas():
    ideas = get_project_ideas(["AWS", "Docker"])
    assert any("cloud" in idea.lower() for idea in ideas)


def test_resume_tips_generic_always_present():
    tips = get_resume_tips([])
    assert len(tips) >= 5


def test_resume_tips_cloud_specific():
    tips = get_resume_tips(["AWS"])
    joined = " ".join(tips).lower()
    assert "cloud" in joined