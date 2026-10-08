"""
CareerIQ - Visualizations
-------------------------
Matplotlib / Seaborn charts for the CareerIQ dashboard:
    - Matched vs Missing skills bar chart
    - Category-wise coverage chart
"""

import matplotlib.pyplot as plt
import seaborn as sns

from data.skills import get_category, get_categories


# ---------------------------------------------------------------
# Style
# ---------------------------------------------------------------
sns.set_style("whitegrid")

COLOR_MATCHED = "#2ecc71"     # green
COLOR_MISSING = "#e74c3c"     # red
COLOR_COVERED = "#3498db"     # blue
COLOR_UNCOVERED = "#bdc3c7"   # gray


# ---------------------------------------------------------------
# Chart 1: Matched vs Missing
# ---------------------------------------------------------------
def plot_matched_vs_missing(matched, missing):
    """
    Bar chart showing matched and missing skill counts.

    Args:
        matched (list[str]): Matched skills.
        missing (list[str]): Missing skills.

    Returns:
        matplotlib.figure.Figure
    """
    fig, ax = plt.subplots(figsize=(6, 4))

    labels = ["Matched", "Missing"]
    values = [len(matched), len(missing)]
    colors = [COLOR_MATCHED, COLOR_MISSING]

    bars = ax.bar(labels, values, color=colors, width=0.5)

    # Annotate counts
    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(value),
            ha="center",
            fontsize=12,
            fontweight="bold",
        )

    ax.set_title("Skills Overview", fontsize=13, fontweight="bold")
    ax.set_ylabel("Number of Skills")
    ax.set_ylim(0, max(values) + 1 if max(values) > 0 else 1)

    sns.despine()
    fig.tight_layout()
    return fig


# ---------------------------------------------------------------
# Chart 2: Category-wise Coverage
# ---------------------------------------------------------------
def compute_category_coverage(resume_skills, required_skills):
    """
    Compute match percentage per skill category.

    Args:
        resume_skills (list[str]): Skills from resume.
        required_skills (list[str]): Skills required by JD.

    Returns:
        dict[str, float]: {category: coverage_percent (0-100)}
    """
    resume_set = set(resume_skills or [])
    required_set = set(required_skills or [])

    coverage = {}

    for category in get_categories():
        required_in_cat = {
            s for s in required_set if get_category(s) == category
        }
        if not required_in_cat:
            continue

        matched_in_cat = required_in_cat & resume_set
        percent = round((len(matched_in_cat) / len(required_in_cat)) * 100, 1)
        coverage[category] = percent

    return coverage


def plot_category_coverage(coverage):
    """
    Horizontal bar chart showing coverage % per category.

    Args:
        coverage (dict[str, float]): Output of compute_category_coverage.

    Returns:
        matplotlib.figure.Figure or None (if no data)
    """
    if not coverage:
        return None

    # Sort ascending so highest is on top when horizontal
    items = sorted(coverage.items(), key=lambda x: x[1])
    categories = [k for k, _ in items]
    values = [v for _, v in items]

    colors = [
        COLOR_MATCHED if v >= 75
        else "#f39c12" if v >= 50
        else COLOR_MISSING
        for v in values
    ]

    fig, ax = plt.subplots(figsize=(7, max(3, 0.5 * len(categories))))

    bars = ax.barh(categories, values, color=colors)

    for bar, value in zip(bars, values):
        ax.text(
            value + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{value}%",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_xlim(0, 110)
    ax.set_xlabel("Coverage (%)")
    ax.set_title(
        "Category-wise Skill Coverage",
        fontsize=13,
        fontweight="bold"
    )

    sns.despine()
    fig.tight_layout()
    return fig