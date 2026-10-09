CareerIQ 💼

CareerIQ is an AI-powered career intelligence platform that analyzes resumes against job descriptions to identify skill gaps, calculate job match scores, predict suitable career roles, and provide personalized career recommendations.

GitHub Repository: CareerIQ Repo

🛠 Tech Stack
Language: Python
Web Framework: Streamlit
Data Processing: Pandas + NumPy
Machine Learning: Scikit-learn
NLP: TF-IDF Vectorization
PDF Processing: PyMuPDF
Visualization: Matplotlib + Seaborn
Model Persistence: Joblib
Development: Jupyter Notebook + VS Code
⚡ Features
Resume Analysis:
Extract text from PDF resumes
Identify technical skills using a skill dictionary and aliases
Analyze resume content and skill distribution
Estimate resume quality using a machine learning model
Job Matching:
Compare resume skills with a target job description
Calculate a job match score
Identify matched and missing skills
Prioritize skill gaps as Critical, Important, or Nice to Have
Machine Learning:
Predict suitable career roles using a Random Forest Classifier
Estimate resume quality using a Gradient Boosting Regressor
Discover similar resume profiles using K-Means clustering and cosine similarity
Convert resume text into numerical features using TF-IDF
Career Recommendations:
Suggest skills to learn based on identified gaps
Recommend relevant project ideas
Provide resume improvement tips
Visualize matched skills and missing skills through charts
🧠 Machine Learning Models
Random Forest Classifier: Predicts career categories from resume text.
Gradient Boosting Regressor: Estimates resume quality scores using handcrafted features.
K-Means Clustering: Groups similar resume profiles.
TF-IDF Vectorization: Converts resume text into numerical features for classification.
Cosine Similarity: Identifies resumes with similar text representations.
📊 Model Performance

The current experimental results for the career role classifier are:

Accuracy: 74.25%
Macro F1 Score: 0.6913
Weighted F1 Score: 0.7260
Training Samples: 1,987
Test Samples: 497
Job Categories: 24

The reported resume quality scorer achieved an R² score of 0.9931. This result should be interpreted in the context of the scoring methodology and verified against the model evaluation notebook.

📂 Project Structure
careeriq/
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
├── data/
│   ├── skills.py
│   ├── raw/
│   │   └── resumes.csv
│   └── processed/
│       └── features.npz
├── models/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_role_classifier.ipynb
│   ├── 03_tfidf_classifier.ipynb
│   ├── 04_quality_scorer.ipynb
│   └── 05_similar_profiles.ipynb
├── tests/
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md

🚀 Installation and Setup
1. Clone the Repository
git clone https://github.com/amritrai404/careeriq.git
cd careeriq

2. Create a Virtual Environment

Windows:

python -m venv .venv
.venv\Scripts\Activate.ps1


Linux/macOS:

python -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Download the Dataset

Download the resume dataset from Kaggle Resume Dataset.

Place the dataset at data/raw/resumes.csv if required by the project configuration.

5. Run the Application
streamlit run streamlit_app.py


Open http://localhost:8501 in your browser.

🧪 Running Tests

Run the test suite using:

pytest -v


The tests cover resume parsing, skill extraction, skill matching, skill gap prioritization, and career recommendations.

🔮 Future Improvements
Integrate semantic similarity using Sentence-BERT embeddings
Add LLM-powered personalized career guidance
Support multilingual resumes
Add OCR support for scanned PDF resumes
Develop a FastAPI backend
Containerize the application using Docker
Expand the skill database
Improve model explainability and confidence calibration
👨‍💻 Author

Amrit Rai

GitHub: @amritrai404
Project: CareerIQ Repository
⚠️ Disclaimer

CareerIQ is designed for educational and career-assistance purposes. Its match scores, predictions, and resume quality estimates are not guarantees of hiring outcomes. Model performance depends on the training dataset, evaluation methodology, and input quality.

⭐ If you find this project useful, consider giving the repository a star!
