💼 CareerIQ
AI-Powered Career Intelligence Platform

<p align="center"> <b>Turn your resume into a smarter career roadmap.</b> <br /> Analyze skills, discover gaps, predict career roles, and get personalized recommendations. </p>

<p align="center"> <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /> <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Machine Learning" /> <img src="https://img.shields.io/badge/Status-In%20Development-blue?style=for-the-badge" alt="Project Status" /> </p>

<p align="center"> <a href="https://github.com/amritrai404/careeriq">Repository</a> • <a href="#-features">Features</a> • <a href="#-installation">Installation</a> • <a href="#-model-performance">Model Performance</a> </p>

📌 Overview

CareerIQ is an AI-powered career intelligence platform designed to help job seekers understand how well their resumes align with a target job description.

It combines resume parsing, skill extraction, machine learning, and personalized recommendations to provide actionable career insights.

Resume + Job Description → Skill Analysis → Match Score → Skill Gaps → Career Roadmap
✨ Features

<table> <tr> <td width="50%"> <h3>📄 Resume Analysis</h3> Extract text from PDF resumes and identify relevant skills using rule-based NLP techniques. </td> <td width="50%"> <h3>🎯 Job Matching</h3> Compare resume skills against job requirements and calculate a match score. </td> </tr> <tr> <td width="50%"> <h3>🧠 Career Prediction</h3> Predict suitable career categories using a Random Forest classification model. </td> <td width="50%"> <h3>📊 Skill Gap Analysis</h3> Identify missing skills and organize them by priority. </td> </tr> <tr> <td width="50%"> <h3>📈 Resume Quality Scoring</h3> Estimate resume quality using handcrafted features and a regression model. </td> <td width="50%"> <h3>👥 Similar Profiles</h3> Discover similar resumes using clustering and text similarity techniques. </td> </tr> <tr> <td width="50%"> <h3>📚 Career Recommendations</h3> Generate learning suggestions, project ideas, and resume improvement tips. </td> <td width="50%"> <h3>📉 Visual Analytics</h3> Explore matched skills, missing skills, and skill coverage through charts. </td> </tr> </table>

🎯 The Problem

Job seekers frequently face questions such as:

How closely does my resume match a particular job?
Which important skills am I missing?
Which career categories align with my current skill set?
What should I learn next?
How can I improve my resume for a specific opportunity?

Traditional resume tools often focus on formatting or basic keyword matching.

CareerIQ aims to bring these insights together in one workflow.

💡 How It Works
flowchart TD
    A[Resume PDF] --> C[Text Extraction]
    B[Job Description] --> D[JD Processing]
    C --> E[Skill Extraction]
    D --> F[Required Skills]
    E --> G[Skill Matching]
    F --> G
    G --> H[Match Score]
    G --> I[Missing Skills]
    C --> J[ML Role Prediction]
    C --> K[Resume Quality Scoring]
    C --> L[Similar Profile Discovery]
    H --> M[Career Insights]
    I --> M
    J --> M
    K --> M
    L --> M
    M --> N[Recommendations and Visualizations]

Workflow
Upload: Provide a resume in PDF format.
Analyze: Extract resume text and identify skills.
Compare: Match extracted skills against job requirements.
Predict: Use trained ML models for career role prediction and quality estimation.
Recommend: Display skill gaps, learning suggestions, and resume improvement tips.
🧪 Machine Learning Techniques
Technique	Application
TF-IDF Vectorization	Converts resume text into numerical features
Random Forest Classifier	Predicts career categories
Gradient Boosting Regressor	Estimates resume quality scores
K-Means Clustering	Groups similar resume profiles
Truncated SVD	Reduces dimensionality of sparse text features
Cosine Similarity	Measures similarity between resume vectors
Stratified Train/Test Split	Maintains class distribution during evaluation
Feature Importance	Helps interpret classification predictions
📊 Model Performance
Career Role Classification

The following figures are the reported experimental results and should be verified against the training notebook before publication.

<p align="center"> <img src="https://img.shields.io/badge/Reported%20Accuracy-74.25%25-success?style=for-the-badge" alt="Reported Accuracy: 74.25%" /> <img src="https://img.shields.io/badge/Job%20Categories-24-blue?style=for-the-badge" alt="24 Job Categories" /> <img src="https://img.shields.io/badge/TF--IDF%20Features-2000-orange?style=for-the-badge" alt="2000 TF-IDF Features" /> </p>

Metric	Reported Result
Accuracy	74.25%
Macro F1 Score	0.6913
Weighted F1 Score	0.7260
Training Samples	1,987
Test Samples	497
Job Categories	24
Resume Quality Scoring
Metric	Reported Result
Model	Gradient Boosting Regressor
MAE	0.46
R² Score	0.9931
Input Features	8

Note: Resume quality metrics should be interpreted in the context of how the target score was generated and evaluated. These values do not establish real-world hiring success.

Similar Profile Discovery
Component	Configuration
Clustering Algorithm	K-Means
Number of Clusters	10
Dimensionality Reduction	Truncated SVD
SVD Components	50
Similarity Metric	Cosine Similarity
🛠️ Tech Stack

<p> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" /> <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" /> <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="Scikit-learn" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" /> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter" /> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" /> </p>

Category	Tools
Language	Python
Interface	Streamlit
Data Processing	Pandas, NumPy
Machine Learning	Scikit-learn
PDF Parsing	PyMuPDF
Visualization	Matplotlib, Seaborn
Model Persistence	Joblib
Testing	Pytest
Development	VS Code, Jupyter Notebook
Version Control	Git, GitHub
📁 Project Structure
careeriq/
│
├── app/
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

Ensure this structure matches the files actually present in your repository. Raw datasets and trained model files may be excluded from version control.
🚀 Installation
Prerequisites
Python 3.11 or newer
Git
VS Code or another Python editor
1. Clone the Repository
git clone https://github.com/amritrai404/careeriq.git
cd careeriq

2. Create a Virtual Environment

Windows — PowerShell

python -m venv .venv
.venv\Scripts\Activate.ps1


Linux / macOS

python -m venv .venv
source .venv/bin/activate

3. Install Dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

4. Download the Dataset

Download the dataset from Kaggle:

📥 Resume Dataset — Kaggle

Place the CSV file in the location expected by your project:

data/raw/resumes.csv


Check that the filename and column names match the code.

5. Launch CareerIQ
streamlit run streamlit_app.py


Open the local URL shown in your terminal, usually:

http://localhost:8501

📚 Dataset

Source: Kaggle Resume Dataset

Property	Details
Total Resumes	2,484
Job Categories	24
Text Columns	Resume_str, Resume_html
Target Column	Category
Identifier	ID
Categories

HR, Designer, Information Technology, Teacher, Advocate, Business Development, Healthcare, Fitness, Agriculture, BPO, Sales, Consultant, Digital Media, Automobile, Chef, Finance, Apparel, Engineering, Accountant, Construction, Public Relations, Banking, Arts, and Aviation.

Dataset note: Review the source's current licensing terms before redistributing the dataset or including its contents in a public repository.

🔬 Model Training

Model development and experimentation are organized into Jupyter notebooks.

Notebook	Description
01_eda.ipynb	Exploratory data analysis and skill feature extraction
02_role_classifier.ipynb	Baseline role classifier
03_tfidf_classifier.ipynb	TF-IDF-based role classification
04_quality_scorer.ipynb	Resume quality scoring
05_similar_profiles.ipynb	Clustering and dimensionality reduction

Run notebooks in the correct order, ensuring the required datasets and dependencies are available.

📌 Project Roadmap
Feature	Status
Resume PDF Parsing	Verify current implementation
Skill Extraction	Verify current implementation
Job Description Matching	Verify current implementation
Skill Gap Prioritization	Verify current implementation
Career Recommendations	Verify current implementation
Visual Analytics	Verify current implementation
ML Role Classification	Reported experimental result
Resume Quality Scoring	Verify evaluation
Similar Profile Discovery	Verify current implementation
LLM-Powered Guidance	Planned
FastAPI Backend	Planned
Docker Deployment	Planned
Multilingual Resume Support	Planned
🔮 Future Improvements
Semantic matching using Sentence-BERT embeddings.
LLM-powered personalized career guidance.
Multilingual resume analysis.
OCR support for scanned PDFs.
Resume comparison and bulk analysis.
Analysis history using SQLite or PostgreSQL.
FastAPI endpoints for integration.
Docker-based deployment.
An expanded skill database.
Better model calibration and explainability.
🧪 Testing

Run the test suite:

pytest -v


Tests are intended to cover:

PDF text extraction.
Skill extraction and aliases.
Case-insensitive matching.
Duplicate handling and word boundaries.
Matched and missing skill identification.
Empty inputs and invalid files.
Skill gap prioritization.
Recommendation generation.

The actual test results depend on the current code and environment.

👨‍💻 Author

Amrit Rai

<p> <a href="https://github.com/amritrai404"> <img src="https://img.shields.io/badge/GitHub-amritrai404-181717?style=for-the-badge&logo=github" alt="GitHub Profile" /> </a> <a href="https://github.com/amritrai404/careeriq"> <img src="https://img.shields.io/badge/Project-CareerIQ-2ea44f?style=for-the-badge&logo=github" alt="CareerIQ Repository" /> </a> </p>

🙏 Acknowledgements
Kaggle — Resume dataset.
Streamlit — Web application framework.
Scikit-learn — Machine learning tools.
PyMuPDF — PDF text extraction.
⚠️ Disclaimer

CareerIQ is designed for educational and career-assistance purposes.

Its match scores, predictions, and resume quality estimates are not guarantees of hiring success. Model performance depends on the training dataset, evaluation methodology, and quality of input data.

Use the generated insights as guidance, alongside human judgment and professional career advice.

<p align="center"> <b>Built with Python, Machine Learning, and a passion for learning. 🚀</b> <br /><br /> ⭐ If you find CareerIQ useful, consider starring the repository! </p>
