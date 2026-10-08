"""
CareerIQ - Career Recommendations
---------------------------------
Generates personalized learning suggestions, project ideas,
and resume improvement tips based on missing skills.
"""

from data.skills import get_category


# ---------------------------------------------------------------
# Skill -> Learning Suggestion Map
# ---------------------------------------------------------------
LEARNING_SUGGESTIONS = {
    # Programming
    "Python": "Practice Python fundamentals and build small CLI projects.",
    "Java": "Learn Java OOP concepts and build a small Spring Boot app.",
    "JavaScript": "Master ES6+ features and build interactive web pages.",
    "TypeScript": "Learn TypeScript types and convert a JS project to TS.",
    "C++": "Practice DSA problems in C++ on LeetCode.",
    "Go": "Build a simple REST API in Go using net/http.",
    "R": "Practice R for statistics and data visualization.",

    # Data Science
    "Pandas": "Complete a Pandas tutorial and analyze a Kaggle dataset.",
    "NumPy": "Practice NumPy array operations and vectorization.",
    "Data Analysis": "Work on an end-to-end EDA project with a real dataset.",
    "Data Visualization": "Build dashboards with Matplotlib and Seaborn.",
    "Statistics": "Revise descriptive and inferential statistics basics.",
    "Power BI": "Build a Power BI dashboard from a public dataset.",
    "Tableau": "Create a Tableau storyboard from a sample dataset.",
    "Excel": "Practice pivot tables, VLOOKUP, and Excel charts.",
    "SQL": "Practice SQL joins, subqueries, and window functions.",

    # ML / AI
    "Machine Learning": "Complete Andrew Ng's ML course and build 2 ML projects.",
    "Deep Learning": "Learn neural networks and train a small CNN on MNIST.",
    "Scikit-learn": "Build classification and regression models with sklearn.",
    "TensorFlow": "Train a simple neural network using TensorFlow/Keras.",
    "PyTorch": "Complete PyTorch's 60-minute blitz tutorial.",
    "Natural Language Processing": "Build a text classifier or sentiment analysis project.",
    "Computer Vision": "Train an image classifier on CIFAR-10.",
    "Generative AI": "Explore LLM APIs and build a small chatbot.",
    "Large Language Models": "Learn prompt engineering and LLM API usage.",
    "RAG": "Build a document Q&A app using LangChain + vector DB.",
    "LangChain": "Build a simple chain-based LLM application.",
    "Prompt Engineering": "Practice prompt patterns for reliable LLM outputs.",
    "Transformers": "Study attention mechanism and fine-tune a small model.",
    "Hugging Face": "Explore Hugging Face models and pipelines.",

    # Web
    "HTML": "Build a static portfolio website using HTML.",
    "CSS": "Style your portfolio with modern CSS and Flexbox/Grid.",
    "React": "Build a todo app or weather app using React.",
    "Next.js": "Convert a React project to Next.js with routing.",
    "Node.js": "Build a REST API using Node.js and Express.",
    "Django": "Build a small blog app using Django.",
    "Flask": "Build a simple REST API with Flask.",
    "FastAPI": "Build a REST API with FastAPI and Pydantic models.",
    "REST API": "Design and document a REST API using Postman/Swagger.",
    "GraphQL": "Build a small GraphQL server with Apollo.",

    # Databases
    "MySQL": "Practice SQL queries and database design in MySQL.",
    "PostgreSQL": "Learn PostgreSQL-specific features and indexing.",
    "MongoDB": "Build a CRUD app using MongoDB and Mongoose.",
    "Redis": "Learn caching basics and use Redis in a small project.",
    "Database Design": "Practice normalization and ER diagram design.",

    # Cloud / DevOps
    "AWS": "Complete AWS Cloud Practitioner essentials and deploy a project on EC2.",
    "Azure": "Explore Azure fundamentals and deploy a web app.",
    "Google Cloud": "Try Google Cloud free tier and deploy a small app.",
    "Docker": "Dockerize a Python or Node.js application.",
    "Kubernetes": "Deploy a small app on Minikube to learn Kubernetes basics.",
    "Terraform": "Provision a simple cloud resource using Terraform.",
    "CI/CD": "Set up GitHub Actions to auto-test and deploy a project.",
    "Jenkins": "Build a small Jenkins pipeline for a sample repo.",
    "GitHub Actions": "Automate tests on push using GitHub Actions.",
    "Linux": "Practice basic Linux commands and shell scripting.",
    "Nginx": "Serve a static site or reverse-proxy an API using Nginx.",

    # Tools
    "Git": "Practice branching, merging, and rebasing in a sample repo.",
    "GitHub": "Publish 2–3 polished projects with clear READMEs.",
    "Docker Compose": "Run a multi-service app using Docker Compose.",
    "Jira": "Try Jira with a sample Agile board.",
    "Agile": "Learn Scrum ceremonies: standup, sprint, retro.",
    "Scrum": "Practice backlog grooming and sprint planning.",

    # Soft Skills
    "Communication": "Practice explaining technical ideas in simple language.",
    "Teamwork": "Contribute to an open-source project on GitHub.",
    "Problem Solving": "Solve 2–3 DSA problems daily on LeetCode.",
    "Leadership": "Lead a small project or mentor a peer.",
    "Presentation": "Prepare and present a 5-minute tech talk.",
    "Project Management": "Plan a small project with milestones and deadlines.",
}


# ---------------------------------------------------------------
# Category -> Project Idea
# ---------------------------------------------------------------
PROJECT_IDEAS = {
    "Programming Languages": "Build a CLI tool or automation script.",
    "Data Science & Analytics": "Do an end-to-end EDA + dashboard project.",
    "Machine Learning & AI": "Build and deploy a small ML model with an API.",
    "Web Development": "Build a full-stack CRUD app and deploy it.",
    "Databases": "Design a normalized schema for a real-world use case.",
    "Cloud & DevOps": "Deploy a Dockerized app to a cloud provider.",
    "Tools & Version Control": "Automate tests and linting with CI on GitHub.",
    "Soft Skills": "Join a team project or open-source contribution.",
}


# ---------------------------------------------------------------
# Resume Improvement Tips (generic + skill-aware)
# ---------------------------------------------------------------
GENERIC_RESUME_TIPS = [
    "Add measurable outcomes (e.g., 'improved accuracy by 12%').",
    "Use action verbs: built, designed, optimized, deployed.",
    "Keep resume to 1 page for early-career, 2 pages max.",
    "Add a GitHub / portfolio link at the top.",
    "Tailor the resume to each job description.",
    "Remove outdated or irrelevant technologies.",
]


# ---------------------------------------------------------------
# Core API
# ---------------------------------------------------------------
def get_learning_suggestions(missing_skills):
    """
    Return learning suggestions for the given missing skills.

    Args:
        missing_skills (list[str]): Skills missing from resume.

    Returns:
        list[dict]: [{"skill": str, "category": str, "suggestion": str}]
    """
    suggestions = []
    for skill in missing_skills:
        suggestion = LEARNING_SUGGESTIONS.get(
            skill,
            f"Learn the fundamentals of {skill} and build a small project."
        )
        suggestions.append({
            "skill": skill,
            "category": get_category(skill) or "Other",
            "suggestion": suggestion,
        })
    return suggestions


def get_project_ideas(missing_skills):
    """
    Suggest project ideas based on categories of missing skills.

    Args:
        missing_skills (list[str]): Skills missing from resume.

    Returns:
        list[str]: Unique project ideas.
    """
    categories = {get_category(skill) for skill in missing_skills}
    ideas = []
    for category in categories:
        if category in PROJECT_IDEAS:
            ideas.append(PROJECT_IDEAS[category])
    return ideas


def get_resume_tips(missing_skills):
    """
    Return resume improvement tips (generic + skill-aware).

    Args:
        missing_skills (list[str]): Skills missing from resume.

    Returns:
        list[str]: Resume tips.
    """
    tips = list(GENERIC_RESUME_TIPS)

    # Skill-aware additions
    skill_set = set(missing_skills)
    if {"AWS", "Azure", "Google Cloud"} & skill_set:
        tips.append(
            "Highlight any cloud deployments, even personal projects."
        )
    if {"Docker", "Kubernetes"} & skill_set:
        tips.append(
            "Mention any containerized projects or Dockerfiles you've written."
        )
    if {"Machine Learning", "Deep Learning"} & skill_set:
        tips.append(
            "Add ML project links with dataset, model, and accuracy metrics."
        )
    if {"SQL", "MySQL", "PostgreSQL"} & skill_set:
        tips.append(
            "Mention query optimization or complex joins you've worked on."
        )

    return tips