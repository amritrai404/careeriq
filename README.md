# 🚀 CareerIQ

### AI-Powered Career Intelligence Platform

CareerIQ is an AI-powered career intelligence platform that analyzes a user's **resume and target job description** to identify skill gaps, measure job alignment, predict suitable career roles, and provide personalized career recommendations.

> **Resume → Skill Analysis → Job Matching → Career Insights → Personalized Roadmap**

---

## 🎯 Problem

Job seekers often struggle to understand:

- How well their resume matches a specific job
- Which skills they are missing
- Which career roles best fit their current skill set
- What they should learn next
- How to improve their resume for a target role

Most resume tools focus primarily on keyword matching or resume formatting.

**CareerIQ aims to go further by combining Natural Language Processing, Machine Learning, and Generative AI into a single career analysis workflow.**

---

## 💡 Solution

CareerIQ takes:

```
Resume (PDF)
+
Job Description
```

and processes them through an intelligent analysis pipeline:

```
Resume PDF
     │
     ▼
PDF Text Extraction
     │
     ▼
Text Cleaning
     │
     ▼
Skill Extraction
     │
     ├───────────────┐
     │               │
     ▼               ▼
Resume Skills    Job Skills
     │               │
     └───────┬───────┘
             ▼
       Skill Matching
             │
       ┌─────┴─────┐
       ▼           ▼
  Skill Gaps    TF-IDF
                   │
                   ▼
           Cosine Similarity
                   │
                   ▼
            Overall Match
                   │
                   ▼
          Career Role Prediction
                   │
                   ▼
          Career Readiness
                   │
                   ▼
          Generative AI Layer
                   │
                   ▼
      Recommendations + Roadmap
```

---

## ✨ Key Features

### 📄 Resume Analysis

- Upload a resume in PDF format
- Extract resume text automatically
- Clean and normalize extracted text
- Identify relevant technical skills

### 🎯 Job Matching

CareerIQ compares the resume against a target job description and provides:

- Matched skills
- Missing skills
- Skill match percentage
- Text similarity score
- Overall job alignment score

### 🧠 NLP-Based Similarity

The initial version uses classical NLP techniques:

- TF-IDF
- Cosine Similarity
- Text preprocessing

This provides a measurable similarity score between the resume and job description.

### 🔮 Career Role Prediction

A Machine Learning model analyzes the user's skill profile and predicts suitable career roles such as:

- AI Engineer
- ML Engineer
- Data Scientist
- Data Analyst
- Backend Developer

The role prediction system is designed as a supervised classification problem using skill-based feature vectors.

### 📈 Career Readiness

CareerIQ evaluates the user's current skills against the requirements of a target role and generates a career readiness score.

Example:

```
Target Role: AI Engineer

Career Readiness: 72%

Strong Areas:
✓ Python
✓ SQL
✓ Machine Learning

Skill Gaps:
✗ FastAPI
✗ Docker
✗ RAG
✗ AWS
```

### 🤖 Generative AI

The planned AI layer will use an LLM for:

- Personalized recommendations
- Skill-gap explanations
- Learning roadmaps
- Resume improvement suggestions
- Career guidance

Deterministic calculations such as scores, matching, and model predictions will remain in Python/ML logic rather than being delegated entirely to the LLM.

---

## 🧪 Example Output

For a resume containing:

```
Python
SQL
Pandas
Machine Learning
```

and a job requiring:

```
Python
SQL
Machine Learning
FastAPI
Docker
AWS
RAG
```

CareerIQ can identify:

```
🎯 Job Match
57%

✅ Matched Skills
Python
SQL
Machine Learning

❌ Skill Gaps
FastAPI
Docker
AWS
RAG

🔮 Potential Roles
ML Engineer
Data Scientist
AI Engineer
```

> **Note:** Scores shown above are illustrative examples.

---

## 🏗️ System Architecture

```
                       ┌──────────────────┐
                       │      User        │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │    Streamlit     │
                       │    Dashboard     │
                       └────────┬─────────┘
                                │
                                ▼
                       ┌──────────────────┐
                       │     FastAPI      │
                       │   Backend API    │
                       └────────┬─────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
       Resume/NLP              ML              LLM Layer
             │                  │                  │
             ▼                  ▼                  ▼
       PDF Parser        Role Prediction     Recommendations
       Skill Extraction  Match Scoring        Roadmap
       TF-IDF            Readiness            Resume Suggestions
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                         ┌──────────────┐
                         │   Database   │
                         └──────────────┘
```

---

## 🧠 Machine Learning & NLP

CareerIQ applies practical Machine Learning and Natural Language Processing concepts.

### Machine Learning

- Feature Engineering
- Train/Test Split
- Classification
- Logistic Regression
- Random Forest
- Model Evaluation
- Prediction Probabilities

### NLP

- Text Preprocessing
- Keyword-Based Skill Extraction
- TF-IDF Vectorization
- Cosine Similarity

### Generative AI

- LLM Integration
- Structured Output
- Prompt Engineering
- Personalized Recommendations
- Learning Roadmap Generation
- Resume Improvement

---

## 📊 Scoring Approach

CareerIQ separates different types of analysis.

### 1\. Skill Match

```
Matched Required Skills
──────────────────────── × 100
Total Required Skills
```

### 2\. Text Similarity

Resume and job description are converted into TF-IDF vectors and compared using cosine similarity.

```
Resume
   ↓
TF-IDF Vector

Job Description
   ↓
TF-IDF Vector

      ↓

Cosine Similarity
```

### 3\. Overall Match

The initial scoring strategy combines skill coverage and text similarity:

```
Overall Score =
    Skill Match × 0.70
  + Text Similarity × 0.30
```

These weights are configurable and may be improved through future experimentation.

> **Important:** The CareerIQ match score represents resume-to-job alignment. It is not a probability of getting hired.

---

## 🛠️ Tech Stack

| Category | Technology |
| --- | --- |
| Language | Python |
| UI | Streamlit |
| Backend | FastAPI |
| Data Processing | Pandas, NumPy |
| NLP | Scikit-learn |
| Machine Learning | Scikit-learn |
| PDF Processing | PyMuPDF |
| Database | SQLite → PostgreSQL |
| Model Persistence | Joblib |
| Environment Management | python-dotenv |
| Testing | Pytest |
| Containerization | Docker |
| Version Control | Git + GitHub |
| Generative AI | LLM API |
| Deployment | Cloud Platform |

---

## 📁 Project Structure

```
careeriq/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── pdf_parser.py
│   ├── text_cleaner.py
│   ├── skill_extractor.py
│   ├── similarity.py
│   ├── analyzer.py
│   ├── role_predictor.py
│   ├── career_score.py
│   ├── roadmap.py
│   ├── llm_service.py
│   └── utils.py
│
├── data/
│   ├── skills.json
│   ├── roles.csv
│   └── career_profiles.csv
│
├── models/
│   └── role_model.pkl
│
├── tests/
│   ├── test_pdf_parser.py
│   ├── test_skill_extractor.py
│   ├── test_analyzer.py
│   └── test_api.py
│
├── sample_data/
│   ├── sample_resume.pdf
│   └── sample_jobs.txt
│
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1\. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/careeriq.git
cd careeriq
```

### 2\. Create a Virtual Environment

```
python -m venv .venv
```

### 3\. Activate the Environment

#### Windows

```
.venv\Scripts\Activate.ps1
```

#### Linux/macOS

```
source .venv/bin/activate
```

### 4\. Install Dependencies

```
pip install -r requirements.txt
```

### 5\. Run the Application

```
streamlit run streamlit_app.py
```

---

## 🔐 Environment Variables

API keys and other secrets should never be committed to GitHub.

Create a local `.env` file:

```
LLM_API_KEY=your_api_key
```

Make sure `.env` is included in `.gitignore`.

---

## 🧪 Testing

The project will include unit and integration tests covering:

- PDF text extraction
- Text cleaning
- Skill extraction
- Skill matching
- Match score calculation
- Career readiness
- ML predictions
- API responses

Run tests using:

```
pytest
```

---

## 🗺️ Development Roadmap

### Phase 1 — Foundation

- [x]GitHub repository
- [ ]Python virtual environment
- [ ]Project structure
- [ ]Streamlit interface

### Phase 2 — Resume & Job Processing

- [ ]PDF parser
- [ ]Text cleaning
- [ ]Skills database
- [ ]Skill extraction
- [ ]Job description analysis

### Phase 3 — Matching Engine

- [ ]Matched skills
- [ ]Missing skills
- [ ]Skill match score
- [ ]TF-IDF similarity
- [ ]Cosine similarity
- [ ]Combined match score

### Phase 4 — Machine Learning

- [ ]Career role dataset
- [ ]Feature engineering
- [ ]Logistic Regression baseline
- [ ]Random Forest
- [ ]Model evaluation
- [ ]Model persistence
- [ ]Role probability ranking

### Phase 5 — Career Intelligence

- [ ]Career readiness score
- [ ]Similar career profiles
- [ ]Skill prioritization
- [ ]Personalized career analysis

### Phase 6 — Generative AI

- [ ]LLM integration
- [ ]Structured output
- [ ]AI recommendations
- [ ]Personalized learning roadmap
- [ ]Resume improvement

### Phase 7 — Backend & Data

- [ ]FastAPI
- [ ]REST API
- [ ]SQLite
- [ ]Analysis history
- [ ]PostgreSQL migration

### Phase 8 — Production

- [ ]Automated testing
- [ ]Error handling
- [ ]Docker
- [ ]Documentation
- [ ]Deployment
- [ ]Live demo

---

## 🔬 Future Improvements

Potential future versions may include:

- Semantic embeddings
- Transformer-based NLP
- Better skill/entity recognition
- Resume section detection
- OCR for scanned resumes
- Job recommendation system
- Skill dependency graphs
- Larger and more representative ML datasets
- Model calibration
- Resume ranking
- Multi-language resume support

---

## ⚠️ Current Limitations

CareerIQ is being developed incrementally.

The initial version will rely on:

- A curated skills database
- Keyword-based skill extraction
- TF-IDF text similarity
- A limited career-role dataset

Therefore, early model predictions and scores should be considered **experimental rather than production-grade hiring assessments**.

The ML dataset will be expanded and evaluated as the project evolves.

---

## 🎓 What This Project Demonstrates

CareerIQ demonstrates the practical integration of:

```
Python
   ↓
Data Processing
   ↓
Machine Learning
   ↓
Natural Language Processing
   ↓
Feature Engineering
   ↓
Model Evaluation
   ↓
Generative AI
   ↓
API Development
   ↓
Database
   ↓
Testing
   ↓
Docker
   ↓
Deployment
```

Rather than building an isolated ML model, the goal is to demonstrate how ML and NLP components can be integrated into a complete software product.

---

## 📌 Project Status

🚧 **Currently in Active Development**

The project is being built incrementally, starting with the core resume and job-description analysis pipeline and progressing toward a complete AI-powered career intelligence platform.

---

## ⚠️ Disclaimer

CareerIQ is intended as a career-assistance and learning tool.

Its scores and predictions should not be interpreted as guaranteed hiring outcomes or professional employment decisions.

---
