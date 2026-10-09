````markdown
# 💼 CareerIQ

**AI-powered Career Intelligence Platform**

CareerIQ analyzes a resume against a target job description to identify
skill gaps, measure job alignment, predict suitable career roles, and
generate personalized career recommendations.

> **Resume + Job Description → Skill Matching → Match Score → Skill Gaps → Career Recommendations**

---

## 📖 Table of Contents

- [Problem](#-problem)
- [Solution](#-solution)
- [Key Features](#-key-features)
- [ML Techniques](#-ml-techniques)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Dataset](#-dataset)
- [Model Training](#-model-training)
- [Model Performance](#-model-performance)
- [Example Output](#-example-output)
- [Running Tests](#-running-tests)
- [Future Improvements](#-future-improvements)
- [Project Status](#-project-status)
- [Author](#-author)
- [Disclaimer](#-disclaimer)

---

## 🎯 Problem

Job seekers often struggle to answer basic but critical questions:

- **How well does my resume match this specific job?**
- **Which skills am I missing?**
- **Which career roles best fit my current skill set?**
- **What should I learn next to become a stronger candidate?**
- **How can I improve my resume for a target role?**

Most existing resume tools focus only on **formatting** or **keyword matching**.
They do not combine skill analysis, ML-based role prediction, personalized
recommendations, and visual analytics into one workflow.

---

## 💡 Solution

**CareerIQ** takes two inputs:

1. A **resume** (PDF)
2. A **target job description** (text)

and produces:

- A **match score** (0-100%)
- **Matched** and **missing** skills
- **Skill gap priority** (🔴 Critical / 🟡 Important / 🟢 Nice to Have)
- **Predicted career roles** with confidence scores (ML)
- A **resume quality score** (ML)
- **Similar profiles** from a real dataset (ML)
- **Personalized learning path**, **project ideas**, and **resume tips**
- **Visual analytics** (matched vs missing, category-wise coverage)

---

## ✨ Key Features

### Core Analysis (Rule-based NLP)

- 📄 **Resume Parsing** — Extracts clean text from PDF resumes using **PyMuPDF**
- 🧠 **Skill Extraction** — Detects **121+ skills** with aliases (e.g., `ml` → Machine Learning, `k8s` → Kubernetes, `sklearn` → Scikit-learn)
- 🎯 **Job Matching** — Computes match score, matched skills, and missing skills using **set operations**
- 📊 **Skill Gap Priority** — Categorizes missing skills into **Critical / Important / Nice to Have** based on JD frequency
- 📚 **Career Recommendations** — Learning suggestions, project ideas, and resume improvement tips
- 📈 **Visual Analytics** — Matched vs Missing bar chart + Category-wise coverage chart

### ML-Powered Insights

- 🎯 **Career Role Prediction** — **Random Forest Classifier** trained on 2,484 labeled resumes across **24 job categories** (74% accuracy)
- 📊 **Resume Quality Score** — **Gradient Boosting Regressor** producing a 0-100 score based on 8 hand-crafted features
- 👥 **Similar Profile Discovery** — **K-Means clustering** (k=10) + **TF-IDF cosine similarity** to find similar resumes in the dataset

---

## 🧪 ML Techniques Used

| Technique | Purpose |
|-----------|---------|
| **TF-IDF Vectorization** | Convert resume text to numerical features (2000 features, n-grams, min_df/max_df filtering) |
| **Random Forest Classifier** | Predict career role from resume text |
| **Gradient Boosting Regressor** | Predict resume quality score (0-100) |
| **K-Means Clustering** | Group similar resumes into 10 clusters |
| **Truncated SVD** | Dimensionality reduction for sparse TF-IDF (50 components) |
| **Cosine Similarity** | Find similar resumes by comparing TF-IDF vectors |
| **Standard Feature Scaling** | Normalize features for gradient boosting |
| **Train/Test Split (Stratified)** | Preserve class distribution during evaluation |
| **Class Weight Balancing** | Handle class imbalance (5.45x ratio between largest and smallest class) |
| **Feature Importance Analysis** | Interpret which words/skills drive predictions |

---

## 🏗️ Architecture

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
                ┌───────────┴───────────┐
                ↓                       ↓
           Matched Skills          Missing Skills
                │                       │
                └───────────┬───────────┘
                            ↓
                       Match Score
                            ↓
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
   Role Prediction     Quality Score     Similar Profiles
       (RF)              (GBR)              (K-Means)
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ↓
                 Career Recommendations
                            ↓
                   Visual Analytics
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.13 |
| **UI** | Streamlit |
| **PDF Processing** | PyMuPDF (`fitz`) |
| **Data Manipulation** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **NLP** | TF-IDF Vectorization |
| **ML Models** | Random Forest, Gradient Boosting, K-Means, Truncated SVD |
| **Visualization** | Matplotlib, Seaborn |
| **Model Persistence** | Joblib |
| **Testing** | Pytest |
| **Version Control** | Git + GitHub |
| **Development** | Jupyter Notebooks |

---

## 📁 Project Structure

```
careeriq/
│
├── app/                              # Core application code
│   ├── __init__.py
│   ├── resume_parser.py              # PDF → text extraction
│   ├── skill_extractor.py            # Text → skills (regex + dictionary)
│   ├── skill_matcher.py              # Resume vs JD matching
│   ├── skill_gap.py                  # Priority categorization
│   ├── recommendations.py            # Learning path + resume tips
│   ├── visualizations.py             # Matplotlib charts
│   ├── role_predictor.py             # ML: career role prediction
│   ├── quality_features.py           # ML: hand-crafted features
│   ├── quality_scorer.py             # ML: quality score
│   └── profile_matcher.py            # ML: similar profile discovery
│
├── data/
│   ├── __init__.py
│   ├── skills.py                     # Skill database (121 skills, 8 categories)
│   ├── raw/                          # Raw dataset (not in GitHub)
│   │   └── resumes.csv               # Kaggle resume dataset
│   └── processed/                    # Processed features
│       └── features.npz              # Binary skill vectors (2484 × 121)
│
├── models/                           # Trained ML models
│   ├── role_classifier.pkl           # Random Forest classifier (34 MB)
│   ├── quality_regressor.pkl         # Gradient Boosting regressor
│   ├── kmeans_profiles.pkl           # K-Means clustering model
│   ├── tfidf_vectorizer.pkl          # TF-IDF vectorizer
│   ├── svd.pkl                       # Truncated SVD for dimensionality reduction
│   └── pca.pkl                       # PCA (for visualization)
│
├── notebooks/                        # ML training & experimentation
│   ├── 01_eda.ipynb                  # Exploratory Data Analysis
│   ├── 02_role_classifier.ipynb      # Initial Random Forest (skill vector)
│   ├── 03_tfidf_classifier.ipynb     # Improved RF (TF-IDF, 2000 features)
│   ├── 04_quality_scorer.ipynb       # Gradient Boosting Quality Scorer
│   └── 05_similar_profiles.ipynb     # K-Means + SVD
│
├── tests/                            # Unit tests
│   ├── __init__.py
│   ├── test_resume_parser.py
│   ├── test_skill_extractor.py
│   ├── test_skill_matcher.py
│   ├── test_skill_gap.py
│   └── test_recommendations.py
│
├── streamlit_app.py                  # Main Streamlit application
├── requirements.txt                  # Python dependencies
├── .gitignore                        # Git ignore rules
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.11+** (tested on 3.13.7)
- Git
- A code editor (VS Code recommended)

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

### 4. Download the Dataset (Required for Similar Profiles)

1. Go to [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)
2. Download `Resume.csv`
3. Place it at `data/raw/resumes.csv`

**Note:** The dataset is required only for the "Similar Profiles" feature.
Other features (role prediction, quality score, skill matching) work without it.

### 5. Run the Application

```bash
streamlit run streamlit_app.py
```

Open your browser to `http://localhost:8501`.

---

## 📊 Dataset

**Source:** [Resume Dataset by Snehaan Bhawal](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

| Property | Value |
|----------|-------|
| Total Resumes | 2,484 |
| Job Categories | 24 |
| Columns | `ID`, `Resume_str`, `Resume_html`, `Category` |
| Class Imbalance Ratio | 5.45x (largest / smallest class) |
| License | CC0-1.0 (Public Domain) |

**Categories include:** HR, Designer, Information-Technology, Teacher, Advocate,
Business-Development, Healthcare, Fitness, Agriculture, BPO, Sales, Consultant,
Digital-Media, Automobile, Chef, Finance, Apparel, Engineering, Accountant,
Construction, Public-Relations, Banking, Arts, Aviation.

---

## 🔬 Model Training

All ML models are trained in Jupyter notebooks located in `notebooks/`.
Run them **sequentially** to reproduce results.

| Notebook | Purpose | Output |
|----------|---------|--------|
| `01_eda.ipynb` | EDA + Skill feature extraction | `data/processed/features.npz` |
| `02_role_classifier.ipynb` | Initial RF (skill vectors) | Baseline (14% accuracy) |
| `03_tfidf_classifier.ipynb` | Improved RF (TF-IDF, 2000 features) | `role_classifier.pkl` (74% accuracy) |
| `04_quality_scorer.ipynb` | Gradient Boosting Quality Scorer | `quality_regressor.pkl` |
| `05_similar_profiles.ipynb` | K-Means + Truncated SVD | `kmeans_profiles.pkl`, `svd.pkl` |

**Training time:** ~10-15 minutes total (on a standard laptop).

---

## 🎯 Model Performance

### Career Role Classifier (Random Forest)

| Metric | Value |
|--------|-------|
| **Accuracy** | **74.25%** |
| F1 (macro) | 0.6913 |
| F1 (weighted) | 0.7260 |
| Training Samples | 1,987 |
| Test Samples | 497 |
| Features | 2,000 (TF-IDF) |
| Classes | 24 |

**Per-category F1 (Top 5):**

| Category | F1 Score |
|----------|----------|
| CONSTRUCTION | 0.89 |
| DESIGNER | 0.89 |
| CHEF | 0.83 |
| ACCOUNTANT | 0.81 |
| HR | 0.81 |

### Resume Quality Scorer (Gradient Boosting)

| Metric | Value |
|--------|-------|
| **MAE** | **0.46** |
| **R²** | **0.9931** |
| Training Samples | 1,987 |
| Features | 8 hand-crafted |

**Features used:** word count, unique word ratio, skill count,
action verb count, number count, section count, avg word length,
capitalized ratio.

### Similar Profiles (K-Means + SVD)

| Metric | Value |
|--------|-------|
| Clusters (k) | 10 |
| SVD Components | 50 |
| Explained Variance | 33.55% |
| Similarity Metric | Cosine (TF-IDF) |

---

## 📊 Example Output

For a resume containing `Python, SQL, Pandas` and a JD requiring
`Python, SQL, Pandas, AWS, Docker`:

```
🎯 Career Match Score: 60%
Status: 🟡 Moderate Match

🤖 AI-Powered Insights
   🎯 Predicted Career Roles:
      • ENGINEERING — 25.34%
      • CONSULTANT — 5.90%
      • INFORMATION-TECHNOLOGY — 5.55%
   📊 Resume Quality Score: 78.5/100

✅ Matched Skills
   Python  •  SQL  •  Pandas

❌ Missing Skills
   AWS  •  Docker

🎯 Skill Gap Priority
   🔴 Critical     → AWS
   🟡 Important    → Docker
   🟢 Nice to Have → —

👥 Similar Profiles (ML)
   1. INFORMATION-TECHNOLOGY — 42.15%
   2. ENGINEERING — 38.90%
   3. CONSULTANT — 35.22%

📚 Career Recommendations
   🎓 Learning Path:
      • AWS → Complete AWS Cloud Practitioner essentials
      • Docker → Dockerize a Python or Node.js application
   🛠️ Project Ideas:
      • Deploy a Dockerized app to a cloud provider
   📄 Resume Tips:
      • Highlight any cloud deployments, even personal projects
      • Mention containerized projects or Dockerfiles you've written
```

---

## 🧪 Running Tests

```bash
pytest -v
```

Expected output:

```
========================= 25 passed in 0.67s =========================
```

Tests cover:
- PDF text extraction (valid + invalid inputs)
- Skill extraction (case-insensitive, aliases, duplicates, word boundaries)
- Skill matching (matched, missing, extra, empty inputs)
- Skill gap priority (critical, important, nice to have, soft skills)
- Recommendations (learning suggestions, project ideas, resume tips)

---

## 🔮 Future Improvements

- **Semantic similarity** using Sentence-BERT embeddings
- **LLM-powered** personalized career guidance (OpenAI / Anthropic / Llama)
- **Multi-language** resume support
- **Analysis history** with SQLite → PostgreSQL migration
- **FastAPI backend** + REST API endpoints
- **Docker containerization** + cloud deployment
- **Expand skill database** from 121 → 500+ skills
- **OCR support** for scanned PDFs
- **Resume ranking** for recruiters (bulk analysis)
- **Model calibration** for better probability estimates

---

## 📌 Project Status

🚧 **Core platform complete** — Rule-based analysis pipeline + 3 ML models deployed.

| Component | Status |
|-----------|--------|
| PDF Parsing | ✅ |
| Skill Extraction | ✅ |
| Skill Matching | ✅ |
| Skill Gap Priority | ✅ |
| Recommendations | ✅ |
| Visual Analytics | ✅ |
| ML: Role Prediction | ✅ (74%) |
| ML: Quality Score | ✅ |
| ML: Similar Profiles | ✅ |
| LLM Integration | ⏳ Planned |
| FastAPI Backend | ⏳ Planned |
| Docker Deployment | ⏳ Planned |

---

## 👤 Author

**Amrit Rai**

- GitHub: [@amritrai404](https://github.com/amritrai404)
- Project: [CareerIQ](https://github.com/amritrai404/careeriq)

---

## 🙏 Acknowledgements

- Kaggle for the [Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)
- Streamlit for the deployment platform
- Scikit-learn for ML algorithms
- PyMuPDF for PDF parsing

---

## ⚠️ Disclaimer

CareerIQ is intended as a **career-assistance and learning tool**.

Its scores and predictions should **not** be interpreted as guaranteed
hiring outcomes or professional employment decisions. Model accuracy
(74%) reflects the training dataset, not real-world hiring outcomes.

Always combine automated insights with human judgment and personalized
career advice from mentors or professionals.

---

⭐ **If you found this project useful, please consider giving it a star!**
````