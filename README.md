💼 CareerIQ

AI-Powered Career Intelligence Platform

CareerIQ analyzes a resume against a target job description to identify skill gaps, measure job alignment, predict suitable career roles, and generate personalized career recommendations.

Resume + Job Description → Skill Matching → Match Score → Skill Gaps → Career Recommendations
📖 Table of Contents
Problem
Solution
Key Features
ML Techniques
Architecture
Tech Stack
Project Structure
Getting Started
Dataset
Model Training
Model Performance
Example Output
Running Tests
Future Improvements
Project Status
Author
Acknowledgements
Disclaimer
🎯 Problem

Job seekers often struggle to answer basic but critical questions:

How well does my resume match a specific job?
Which skills am I missing?
Which career roles best fit my current skill set?
What should I learn next to become a stronger candidate?
How can I improve my resume for a target role?

Most resume tools focus primarily on formatting or keyword matching. They may not combine skill analysis, ML-based role prediction, personalized recommendations, and visual analytics into a single workflow.

💡 Solution

CareerIQ takes two inputs:

A resume in PDF format.
A target job description in text format.

It then generates:

A job match score from 0–100%.
Matched and missing skills.
Skill gap priorities: Critical, Important, and Nice to Have.
Predicted career roles with confidence scores.
A resume quality score.
Similar profiles from a resume dataset.
Personalized learning paths and project ideas.
Resume improvement recommendations.
Visual analytics for skill matching and category-wise coverage.
✨ Key Features
Core Analysis — Rule-Based NLP
📄 Resume Parsing: Extracts text from PDF resumes using PyMuPDF.
🧠 Skill Extraction: Identifies 121+ skills using a skill dictionary and aliases, such as ml → Machine Learning, k8s → Kubernetes, and sklearn → Scikit-learn.
🎯 Job Matching: Compares resume skills with job requirements to calculate matched and missing skills.
📊 Skill Gap Prioritization: Categorizes missing skills into Critical, Important, and Nice to Have based on job description requirements.
📚 Career Recommendations: Suggests learning resources, project ideas, and resume improvements.
📈 Visual Analytics: Displays matched versus missing skills and category-wise skill coverage.
ML-Powered Insights
🎯 Career Role Prediction: Random Forest Classifier trained on 2,484 labeled resumes across 24 job categories.
📊 Resume Quality Score: Gradient Boosting Regressor estimates a 0–100 score using eight handcrafted features.
👥 Similar Profile Discovery: Combines K-Means clustering and TF-IDF cosine similarity to identify similar resumes.
🧪 ML Techniques Used
Technique	Purpose
TF-IDF Vectorization	Converts resume text into numerical features using up to 2,000 features and n-grams.
Random Forest Classifier	Predicts career roles from resume text.
Gradient Boosting Regressor	Estimates resume quality scores.
K-Means Clustering	Groups resumes into 10 clusters.
Truncated SVD	Reduces the dimensionality of sparse TF-IDF features to 50 components.
Cosine Similarity	Measures similarity between resume vectors.
Feature Scaling	Prepares numerical features for model training where appropriate.
Stratified Train/Test Split	Preserves class distribution during evaluation.
Class Weight Balancing	Helps address class imbalance during classification.
Feature Importance Analysis	Identifies features that influence model predictions.
🏗️ Architecture
                       💼 CareerIQ
                            |
                +-----------+-----------+
                |                       |
           Resume PDF             Job Description
                |                       |
          PDF Extraction           Text Processing
                |                       |
          Skill Extraction       Skill Extraction
                +-----------+-----------+
                            |
                     Skill Matching
                            |
                +-----------+-----------+
                |                       |
           Matched Skills          Missing Skills
                |                       |
                +-----------+-----------+
                            |
                       Match Score
                            |
          +-----------------+-----------------+
          |                 |                 |
    Role Prediction    Quality Score    Similar Profiles
         (RF)              (GBR)             (K-Means)
          |                 |                 |
          +-----------------+-----------------+
                            |
                Career Recommendations
                            |
                   Visual Analytics

🛠️ Tech Stack
Category	Technology
Programming Language	Python 3.13
User Interface	Streamlit
PDF Processing	PyMuPDF (fitz)
Data Manipulation	Pandas, NumPy
Machine Learning	Scikit-learn
NLP	TF-IDF Vectorization
ML Models	Random Forest, Gradient Boosting, K-Means, Truncated SVD
Visualization	Matplotlib, Seaborn
Model Persistence	Joblib
Testing	Pytest
Version Control	Git and GitHub
Development	Jupyter Notebooks
📁 Project Structure
careeriq/
│
├── app/
│   ├── __init__.py
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── skill_matcher.py
│   ├── skill_gap.py
│   ├── recommendations.py
│   ├── visualizations.py
│   ├── role_predictor.py
│   ├── quality_features.py
│   ├── quality_scorer.py
│   └── profile_matcher.py
│
├── data/
│   ├── __init__.py
│   ├── skills.py
│   ├── raw/
│   │   └── resumes.csv
│   └── processed/
│       └── features.npz
│
├── models/
│   ├── role_classifier.pkl
│   ├── quality_regressor.pkl
│   ├── kmeans_profiles.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── svd.pkl
│   └── pca.pkl
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_role_classifier.ipynb
│   ├── 03_tfidf_classifier.ipynb
│   ├── 04_quality_scorer.ipynb
│   └── 05_similar_profiles.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_resume_parser.py
│   ├── test_skill_extractor.py
│   ├── test_skill_matcher.py
│   ├── test_skill_gap.py
│   └── test_recommendations.py
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md


Note: The structure above represents the intended project layout. Ensure that the listed files and models exist in your repository before publishing this documentation.

🚀 Getting Started
Prerequisites
Python 3.11 or newer.
Git.
A code editor such as VS Code.
1. Clone the Repository
git clone https://github.com/amritrai404/careeriq.git
cd careeriq

2. Create a Virtual Environment

Windows — PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1


Linux/macOS

python -m venv .venv
source .venv/bin/activate

3. Install Dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

4. Download the Dataset

Download the resume dataset from Kaggle:

Resume Dataset — Kaggle

Place the downloaded CSV file at:

data/raw/resumes.csv


Make sure the filename and column names match what the project code expects.

Note: Whether the dataset is required at runtime depends on how the similar-profile feature and model-loading pipeline are implemented.

5. Run the Application
streamlit run streamlit_app.py


Open the local URL displayed in your terminal, typically:

http://localhost:8501

📊 Dataset

Source: Resume Dataset by Snehaan Bhawal

Property	Value
Total Resumes	2,484
Job Categories	24
Columns	ID, Resume_str, Resume_html, Category
Class Distribution	Imbalanced
License	Verify the dataset's current license before redistribution.

The categories include:

HR, Designer, Information Technology, Teacher, Advocate, Business Development, Healthcare, Fitness, Agriculture, BPO, Sales, Consultant, Digital Media, Automobile, Chef, Finance, Apparel, Engineering, Accountant, Construction, Public Relations, Banking, Arts, and Aviation.

🔬 Model Training

The machine learning experiments are organized into Jupyter notebooks.

Notebook	Purpose	Expected Output
01_eda.ipynb	Exploratory Data Analysis and skill feature extraction	features.npz
02_role_classifier.ipynb	Baseline role classification using skill features	Baseline classifier
03_tfidf_classifier.ipynb	TF-IDF-based role classification	Role classifier
04_quality_scorer.ipynb	Resume quality score modeling	Quality regressor
05_similar_profiles.ipynb	Clustering and dimensionality reduction	Clustering model and SVD

Run the notebooks in the appropriate order, ensuring that each notebook's dependencies and output paths are satisfied.

Reproducibility note: Training time and model outputs depend on the hardware, dataset, random seeds, and implementation. Run the notebooks to verify the actual results.

🎯 Model Performance
Career Role Classifier — Random Forest

The following metrics are reported project results and should be confirmed by running the evaluation notebook.

Metric	Reported Value
Accuracy	74.25%
Macro F1 Score	0.6913
Weighted F1 Score	0.7260
Training Samples	1,987
Test Samples	497
TF-IDF Features	2,000
Number of Classes	24
Per-Category F1 Scores
Category	F1 Score
Construction	0.89
Designer	0.89
Chef	0.83
Accountant	0.81
HR	0.81
Resume Quality Scorer — Gradient Boosting
Metric	Reported Value
Mean Absolute Error (MAE)	0.46
R² Score	0.9931
Training Samples	1,987
Input Features	8

The handcrafted features include:

Word count.
Unique word ratio.
Skill count.
Action verb count.
Number count.
Section count.
Average word length.
Capitalized word ratio.

Important: These metrics describe the reported experimental results. The quality scorer's MAE and R² are meaningful only when the target score is independently defined and evaluated against a suitable held-out dataset.

Similar Profile Discovery — K-Means and SVD
Metric	Reported Value
Number of Clusters	10
SVD Components	50
Explained Variance	33.55%
Similarity Metric	Cosine Similarity
📊 Example Output

The following is an illustrative example of the kind of output CareerIQ may generate. Values are examples and are not guaranteed predictions from a trained model.

Example input

Resume skills: Python, SQL, Pandas.
Required job skills: Python, SQL, Pandas, AWS, Docker.
Career Match Score: 60%
Status: Moderate Match

AI-Powered Insights

Predicted Career Roles:
  - Engineering
  - Consultant
  - Information Technology

Resume Quality Score: 78.5/100

Matched Skills:
  - Python
  - SQL
  - Pandas

Missing Skills:
  - AWS
  - Docker

Skill Gap Priority:
  - Critical: AWS
  - Important: Docker
  - Nice to Have: None

Similar Profiles:
  - Information Technology
  - Engineering
  - Consultant

Career Recommendations:

Learning Path:
  - Learn AWS Cloud Practitioner fundamentals.
  - Practice Dockerizing a Python application.

Project Ideas:
  - Deploy a Dockerized application to a cloud provider.

Resume Tips:
  - Highlight relevant cloud deployment experience.
  - Include containerized projects and Dockerfiles.


The match score depends on the actual matching formula. For example, three matched skills out of five required skills produce a 60% score if every required skill has equal weight.

🧪 Running Tests

Run the test suite with:

pytest -v


The test suite is intended to cover:

PDF text extraction and invalid inputs.
Case-insensitive skill extraction and aliases.
Duplicate handling and word boundaries.
Matched, missing, and extra skills.
Empty-input handling.
Skill gap priority categorization.
Career recommendations and project suggestions.

The actual number of passing tests and execution time will depend on the current test suite and environment.

🔮 Future Improvements
Semantic Similarity: Integrate Sentence-BERT embeddings for deeper text understanding.
LLM-Powered Guidance: Generate personalized career advice using an LLM.
Multilingual Support: Analyze resumes in multiple languages.
Analysis History: Store previous analyses using SQLite or PostgreSQL.
FastAPI Backend: Expose analysis functionality through REST APIs.
Docker Deployment: Containerize the application for easier deployment.
Expanded Skill Database: Add more skills, aliases, and job-specific competencies.
OCR Support: Process scanned PDF resumes.
Bulk Resume Analysis: Support recruiter workflows for comparing multiple candidates.
Model Calibration: Improve the reliability of classification confidence estimates.
Explainable AI: Show which skills and text features influence predictions.
📌 Project Status

CareerIQ — Resume Analysis and Career Intelligence

The following table represents the intended feature scope. Update the status based on what is implemented and tested in the current repository.

Component	Status
PDF Parsing	Verify implementation
Skill Extraction	Verify implementation
Skill Matching	Verify implementation
Skill Gap Prioritization	Verify implementation
Career Recommendations	Verify implementation
Visual Analytics	Verify implementation
Career Role Prediction	Reported experimental result: 74.25% accuracy
Resume Quality Scoring	Verify evaluation
Similar Profile Discovery	Verify implementation
LLM Integration	Planned
FastAPI Backend	Planned
Docker Deployment	Planned
👤 Author

Amrit Rai

GitHub: @amritrai404
Project Repository: CareerIQ
🙏 Acknowledgements
Kaggle Resume Dataset
Streamlit
Scikit-learn
PyMuPDF
⚠️ Disclaimer

CareerIQ is intended as a career-assistance and educational tool.

Its scores and predictions should not be interpreted as guaranteed hiring outcomes or professional employment decisions. Classification accuracy reflects performance on a particular dataset and evaluation setup; it does not guarantee equivalent performance on real-world resumes.

Resume quality scores are estimates based on the implemented features and scoring methodology. Users should combine automated insights with human judgment and advice from qualified career professionals.

⭐ If you find this project useful, consider giving the repository a star!
