"""
CareerIQ - Skill Database
-------------------------
Central knowledge base of skills used across the platform
for resume parsing, job description analysis, and matching.

Structure:
    SKILL_CATEGORIES  -> dict[category] -> list[canonical skill names]
    SKILL_ALIASES     -> dict[lowercase alias] -> canonical skill name
    ALL_SKILLS        -> flat list of all canonical skills
    SKILL_TO_CATEGORY -> dict[canonical skill] -> category
"""

# ---------------------------------------------------------------
# Skill Categories
# ---------------------------------------------------------------
SKILL_CATEGORIES = {
    "Programming Languages": [
        "Python", "Java", "JavaScript", "TypeScript",
        "C", "C++", "C#", "Go", "Rust", "Ruby", "PHP",
        "Swift", "Kotlin", "R", "Scala", "MATLAB",
        "Perl", "Dart", "Bash", "Shell Scripting",
    ],

    "Data Science & Analytics": [
        "Data Analysis", "Data Visualization", "Data Cleaning",
        "Exploratory Data Analysis", "Statistics",
        "Statistical Analysis", "A/B Testing", "Pandas",
        "NumPy", "Matplotlib", "Seaborn", "Plotly",
        "Power BI", "Tableau", "Excel", "Jupyter",
        "Feature Engineering",
    ],

    "Machine Learning & AI": [
        "Machine Learning", "Deep Learning", "Scikit-learn",
        "TensorFlow", "PyTorch", "Keras", "XGBoost",
        "LightGBM", "Natural Language Processing",
        "Computer Vision", "Reinforcement Learning",
        "Transfer Learning", "Model Deployment", "MLOps",
        "Generative AI", "Large Language Models",
        "Transformers", "Hugging Face", "LangChain",
        "RAG", "Prompt Engineering", "Fine-tuning",
    ],

    "Web Development": [
        "HTML", "CSS", "React", "Next.js", "Angular",
        "Vue", "Node.js", "Express", "Django", "Flask",
        "FastAPI", "REST API", "GraphQL", "Bootstrap",
        "Tailwind CSS", "Redux",
    ],

    "Databases": [
        "SQL", "MySQL", "PostgreSQL", "SQLite",
        "MongoDB", "Redis", "Cassandra", "Oracle",
        "NoSQL", "Database Design", "Query Optimization",
    ],

    "Cloud & DevOps": [
        "AWS", "Azure", "Google Cloud", "EC2", "S3",
        "Lambda", "Docker", "Kubernetes", "Terraform",
        "CI/CD", "Jenkins", "GitHub Actions",
        "Linux", "Nginx",
    ],

    "Tools & Version Control": [
        "Git", "GitHub", "GitLab", "Bitbucket",
        "VS Code", "Postman", "Jira", "Confluence",
        "Agile", "Scrum",
    ],

    "Soft Skills": [
        "Communication", "Teamwork", "Collaboration",
        "Problem Solving", "Critical Thinking",
        "Leadership", "Time Management", "Adaptability",
        "Presentation", "Project Management",
        "Stakeholder Management",
    ],
}


# ---------------------------------------------------------------
# Skill Aliases
# (lowercase alias -> canonical skill name)
# ---------------------------------------------------------------
SKILL_ALIASES = {
    # Programming
    "py": "Python",
    "js": "JavaScript",
    "ts": "TypeScript",
    "golang": "Go",
    "csharp": "C#",
    "c sharp": "C#",

    # Data Science
    "data analytics": "Data Analysis",
    "data viz": "Data Visualization",
    "eda": "Exploratory Data Analysis",
    "stats": "Statistics",
    "powerbi": "Power BI",
    "ms excel": "Excel",
    "microsoft excel": "Excel",

    # ML / AI
    "ml": "Machine Learning",
    "dl": "Deep Learning",
    "sklearn": "Scikit-learn",
    "scikit learn": "Scikit-learn",
    "tf": "TensorFlow",
    "torch": "PyTorch",
    "nlp": "Natural Language Processing",
    "cv": "Computer Vision",
    "llm": "Large Language Models",
    "llms": "Large Language Models",
    "genai": "Generative AI",
    "gen ai": "Generative AI",
    "hf": "Hugging Face",
    "huggingface": "Hugging Face",

    # Web
    "node": "Node.js",
    "nodejs": "Node.js",
    "reactjs": "React",
    "react.js": "React",
    "nextjs": "Next.js",
    "vuejs": "Vue",
    "vue.js": "Vue",
    "rest": "REST API",
    "restful api": "REST API",

    # Databases
    "postgres": "PostgreSQL",
    "psql": "PostgreSQL",
    "mongo": "MongoDB",
    "mongo db": "MongoDB",

    # Cloud
    "gcp": "Google Cloud",
    "google cloud platform": "Google Cloud",
    "amazon web services": "AWS",
    "k8s": "Kubernetes",
    "gh actions": "GitHub Actions",
    "github action": "GitHub Actions",

    # Tools
    "visual studio code": "VS Code",
}


# ---------------------------------------------------------------
# Derived Helpers (built once at import)
# ---------------------------------------------------------------
ALL_SKILLS = [
    skill
    for skills in SKILL_CATEGORIES.values()
    for skill in skills
]

SKILL_TO_CATEGORY = {
    skill: category
    for category, skills in SKILL_CATEGORIES.items()
    for skill in skills
}


# ---------------------------------------------------------------
# Public API
# ---------------------------------------------------------------
def get_all_skills():
    """Return a flat list of every canonical skill."""
    return list(ALL_SKILLS)


def get_category(skill):
    """Return the category a canonical skill belongs to."""
    return SKILL_TO_CATEGORY.get(skill)


def get_skills_by_category(category):
    """Return all skills under a given category."""
    return SKILL_CATEGORIES.get(category, [])


def get_categories():
    """Return all category names."""
    return list(SKILL_CATEGORIES.keys())