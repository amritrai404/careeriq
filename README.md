# CareerIQ 💼

**CareerIQ** is an AI-powered career intelligence platform that analyzes a resume against a target job description to identify skill gaps, predict suitable career roles, and provide personalized career recommendations.

**GitHub Repository:** [CareerIQ Repo](https://github.com/amritrai404/careeriq)  
**Live Demo:** Coming soon

---

## 🛠 Tech Stack

- **Language:** [Python 3.13](https://www.python.org/)
- **UI:** [Streamlit](https://streamlit.io/)
- **PDF Parsing:** [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`)
- **Data:** Pandas, NumPy
- **Machine Learning:** [Scikit-learn](https://scikit-learn.org/)
- **NLP:** TF-IDF Vectorization
- **ML Models:** Random Forest, Gradient Boosting, K-Means, Truncated SVD
- **Visualization:** Matplotlib, Seaborn
- **Testing:** Pytest
- **Model Persistence:** Joblib
- **Development:** Jupyter Notebooks, Git + GitHub

---

## ⚡ Features

### Core Analysis (Rule-based NLP):
- Upload resume in PDF format and paste any job description
- Extract 120+ technical skills from both resume and JD (with aliases like `ml`, `k8s`, `sklearn`)
- Compute an overall **Career Match Score** (0–100%)
- Identify **matched skills** and **missing skills**
- Prioritize skill gaps into 🔴 Critical / 🟡 Important / 🟢 Nice to Have
- Generate personalized **learning path**, **project ideas**, and **resume tips**
- Visualize matched-vs-missing skills and category-wise coverage

### ML-Powered Insights:
- **Career Role Prediction** — Random Forest Classifier trained on 2,484 resumes across 24 job categories (74% accuracy)
- **Resume Quality Score** — Gradient Boosting Regressor producing a 0–100 score
- **Similar Profile Discovery** — K-Means clustering + TF-IDF cosine similarity

---

## 🧪 ML Techniques Used

- ✅ **TF-IDF Vectorization** — 2,000 text features from resume content
- ✅ **Random Forest Classifier** — Career role prediction (24 classes)
- ✅ **Gradient Boosting Regressor** — Resume quality scoring
- ✅ **K-Means Clustering** — Similar profile grouping (k=10)
- ✅ **Truncated SVD** — Dimensionality reduction (50 components)
- ✅ **Cosine Similarity** — Profile matching
- ✅ **Standard Feature Scaling** — Preprocessing
- ✅ **Stratified Train/Test Split** — Preserve class distribution
- ✅ **Class Weight Balancing** — Handle 5.45x class imbalance
- ✅ **Feature Importance Analysis** — Model interpretability

---

## 🏗 Architecture

```
              💼 CareerIQ
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
       ┌───────────┼───────────┐
       ↓           ↓           ↓
  Role         Quality     Similar
  Prediction   Score       Profiles
   (RF)         (GBR)       (K-Means)
       └───────────┼───────────┘
                   ↓
          Recommendations
                   ↓
          Visual Analytics
```

---

## 📁 Project Structure

```
careeriq/
├── app/
│   ├── resume_parser.py         # PDF → text
│   ├── skill_extractor.py       # text → skills
│   ├── skill_matcher.py         # resume vs JD
│   ├── skill_gap.py             # priority categorization
│   ├── recommendations.py       # learning + resume tips
│   ├── visualizations.py        # charts
│   ├── role_predictor.py        # ML: role prediction
│   ├── quality_features.py      # ML: feature extraction
│   ├── quality_scorer.py        # ML: quality score
│   └── profile_matcher.py       # ML: similar profiles
├── data/
│   ├── skills.py                # skill database (121 skills)
│   └── raw/                     # dataset (not pushed to GitHub)
├── models/                      # trained ML models (.pkl)
├── notebooks/                   # ML training notebooks
├── tests/                       # unit tests (25 passed)
├── streamlit_app.py
├── requirements.txt
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

Open your browser at `http://localhost:8501`.

---

## 📊 Dataset

**Source:** [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset) by Snehaan Bhawal

- **2,484 resumes** across **24 job categories**
- Columns: `ID`, `Resume_str`, `Resume_html`, `Category`
- License: CC0-1.0

---

## 🎯 Model Performance

| Model | Task | Metric | Score |
|-------|------|--------|-------|
| Random Forest | Role Prediction (24 classes) | Accuracy | **74.25%** |
| Random Forest | Role Prediction | F1 (macro) | 0.6913 |
| Gradient Boosting | Quality Score | MAE | 0.46 |
| Gradient Boosting | Quality Score | R² | 0.99 |
| K-Means (k=10) | Similar Profiles | SVD explained | 33.55% |

---

## 📊 Example Output

For a resume containing `Python, SQL, Pandas` and a JD requiring `Python, SQL, Pandas, AWS, Docker`:

```
🎯 Career Match Score: 60%
Status: 🟡 Moderate Match

🤖 AI-Powered Insights
   🎯 Predicted Roles:
      • ENGINEERING — 25.34%
      • CONSULTANT — 5.90%
   📊 Resume Quality Score: 78.5/100

✅ Matched:  Python, SQL, Pandas
❌ Missing:  AWS, Docker

🎯 Skill Gap Priority
   🔴 Critical     → AWS
   🟡 Important    → Docker

📚 Career Recommendations
   🎓 Learning:  Deploy a project on AWS EC2
   🛠️ Projects:  Dockerize a Python application
   📄 Resume:    Highlight cloud deployments
```

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

## 🔮 Future Improvements

- Semantic similarity using Sentence-BERT embeddings
- LLM-powered personalized career guidance
- Multi-language resume support
- Analysis history with SQLite → PostgreSQL
- FastAPI backend + REST endpoints
- Docker containerization + cloud deployment
- Expand skill database from 121 → 500+ skills

---

## 👤 Author

**Amrit Rai**
GitHub: [@amritrai404](https://github.com/amritrai404)

---

## ⚠️ Disclaimer

CareerIQ is intended as a career-assistance and learning tool. Its scores and predictions should not be interpreted as guaranteed hiring outcomes or professional employment decisions.
