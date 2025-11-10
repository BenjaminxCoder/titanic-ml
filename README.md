# Titanic ML Survival Predictor

## Overview
This project builds an end-to-end machine learning system that predicts passenger survival on the Titanic using demographic and travel data. It serves as the foundation for production-grade ML pipelines from data preprocessing and model training to API deployment and CI/CD automation.

The goal is to not only reach strong predictive accuracy but also establish proper ML engineering structure for reproducibility, testing, and deployment.

---

## 🎯 Objectives
- Build a reproducible ML pipeline using scikit-learn.
- Achieve at least 0.80 ROC AUC on validation data.
- Serve predictions via a FastAPI REST endpoint.
- Automate tests and linting through CI/CD.
- Package and deploy using Docker for portability.

---

## ⚙️ Core Functionality
1. **Data Ingestion**
   - Load raw Titanic data (CSV).
   - Validate schema and handle missing values.

2. **Feature Engineering**
   - Encode categorical variables (Sex, Embarked, etc.).
   - Scale and normalize numeric features (Age, Fare).

3. **Model Training**
   - Train baseline classifiers (Logistic Regression, Random Forest).
   - Evaluate using ROC AUC, accuracy, and F1-score.

4. **Model Serving**
   - Expose a `/predict` endpoint via FastAPI.
   - Accept passenger attributes and return survival probability and classification.

5. **Automation & Deployment**
   - Unit tests for data processing and API.
   - Docker container for reproducible serving.
   - CI pipeline for linting, testing, and smoke training.

---

## 🧱 Architecture
```
titanic-ml/
  ├── src/
  │   └── titanic/
  │       ├── features.py
  │       ├── model.py
  │       ├── train.py
  │       ├── evaluate.py
  │       └── predict.py
  ├── api/
  │   └── app.py
  ├── tests/
  ├── configs/
  ├── requirements.txt
  ├── Makefile
  └── README.md
```

---

## 🚀 Getting Started
```bash
# 1. Clone repo
git clone https://github.com/<your-username>/titanic-ml.git
cd titanic-ml

# 2. Create environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run training pipeline
python src/titanic/train.py --config configs/baseline.yaml

# 5. Start API
uvicorn api.app:app --reload
```

---

## 📊 Example Input
```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```

## 📈 Example Output
```json
{
  "probability": 0.192,
  "prediction": 0,
  "top_feature": "Sex_male"
}
```

---

## 🔮 Future Enhancements
- Add feature importance via SHAP.
- Integrate MLflow for experiment tracking.
- Deploy to AWS Lambda or Render.
- Add Prometheus metrics endpoint for monitoring.

---