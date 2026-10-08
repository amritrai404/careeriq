```markdown
# 🚀 CareerIQ

**AI-powered Career Intelligence Platform**

CareerIQ analyzes a resume against a target job description to identify
skill gaps, measure job alignment, and provide personalized career
recommendations.

> Resume + Job Description → Skill Matching → Match Score → Skill Gaps → Career Recommendations

---

## 🎯 Problem

Job seekers often struggle to understand:

- How well their resume matches a specific job
- Which skills they are missing
- What they should learn next
- How to improve their resume

Most resume tools focus only on formatting or keyword matching.
CareerIQ goes further by combining **rule-based NLP**, **skill
categorization**, and **actionable recommendations** into one workflow.

---

## ✨ Key Features

- 📄 **Resume Parsing** — Extracts text from PDF resumes using PyMuPDF
- 🧠 **Skill Extraction** — Detects 120+ skills (with aliases like
  `ml`, `k8s`, `sklearn`) from both resume and JD
- 🎯 **Job Matching** — Computes match score, matched skills, missing skills
- 📊 **Skill Gap Priority** — Categorizes missing skills into
  🔴 Critical / 🟡 Important / 🟢 Nice to Have
- 📚 **Career Recommendations** — Personalized learning suggestions,
  project ideas, and resume tips
- 📈 **Visual Analytics** — Matched-vs-Missing bar chart and
  category-wise coverage chart

---

## 🏗️ Architecture

```
              🚀 CareerIQ
                   │
       ┌───────────┴───────────┐
       ↓                       ↓
  Resume PDF              Job Description
       ↓                       ↓
 PDF Extraction          Text Processing
       ↓                       ↓
 Skill Extraction       Skill Extraction
       └───────────┬───────────┘
                   ↓
            Skill Matching
                   ↓
        ┌──────────┴─────────┐
        ↓                    ↓
   Matched Skills      Missing Skills
        │                    │
        └──────────┬─────────┘
                   ↓
              Match Score
                   ↓
          Skill Gap Priority
                   ↓
        Career Recommendations
                   ↓
          Visual Analytics
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| Language | Python 3.13 |
| UI | Streamlit |
| PDF Processing | PyMuPDF (`fitz`) |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Testing | Pytest |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
careeriq/
├── app/
│   ├── __init__.py
│   ├── resume_parser.py        # PDF → text
│   ├── skill_extractor.py      # text → skills
│   ├── skill_matcher.py        # resume vs JD
│   ├── skill_gap.py            # priority categorization
│   ├── recommendations.py      # learning + resume tips
│   └── visualizations.py       # charts
├── data/
│   ├── __init__.py
│   └── skills.py               # skill database (120+ skills)
├── tests/
│   ├── test_resume_parser.py
│   ├── test_skill_extractor.py
│   ├── test_skill_matcher.py
│   ├── test_skill_gap.py
│   └── test_recommendations.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/amritrai404/careeriq.git
cd careeriq
```

### 2. Create and Activate Virtual Environment

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run streamlit_app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## 🧪 Running Tests

```bash
pytest -v
```

Expected output:

```
25 passed in 0.67s
```

---

## 📊 Example Output

For a resume containing `Python, SQL, Pandas` and a JD requiring
`Python, SQL, Pandas, AWS, Docker`:

```
🎯 Career Match Score: 60%
Status: 🟡 Moderate Match

✅ Matched:  Python, SQL, Pandas
❌ Missing:  AWS, Docker

🎯 Skill Gap Priority
   🔴 Critical     → AWS
   🟡 Important    → Docker
   🟢 Nice to Have → —

📚 Career Recommendations
   🎓 Learning:  Deploy a project on AWS EC2
   🛠️ Projects:  Dockerize a Python application
   📄 Resume:    Highlight cloud deployments
```

---

## 🔮 Future Improvements

- Semantic similarity using embeddings (TF-IDF / Sentence-BERT)
- ML-based career role prediction
- LLM-powered personalized career guidance
- Multi-language resume support
- Analysis history with SQLite → PostgreSQL
- FastAPI backend + REST endpoints
- Docker containerization + cloud deployment

---

## 📌 Project Status

🚧 **Actively in development** — Core analysis pipeline complete,
ML and LLM layers planned for future phases.

---

## 👤 Author

**Amrit Rai**
GitHub: [@amritrai404](https://github.com/amritrai404)

---

## ⚠️ Disclaimer

CareerIQ is intended as a career-assistance and learning tool.
Its scores and predictions should not be interpreted as guaranteed
hiring outcomes or professional employment decisions.
```

---