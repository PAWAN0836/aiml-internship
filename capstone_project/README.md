# AI/ML Internship – Student Performance Prediction

## 📌 Overview

This repository contains the projects and assignments completed during my 2-month Artificial Intelligence and Machine Learning Training & Internship.

The internship covered Python programming, NumPy, Pandas, data preprocessing, visualization, supervised learning, unsupervised learning, feature engineering, feature scaling, model evaluation, hyperparameter tuning, and deployment of an ML model using Flask.

---

## 🎯 Internship Objectives

- Learn Python fundamentals for AI/ML
- Understand data structures and numerical computation
- Perform data preprocessing
- Work with Pandas DataFrames
- Visualize data using Matplotlib
- Understand features and target variables
- Build supervised machine learning models
- Perform regression and classification
- Implement unsupervised learning using K-Means
- Perform feature engineering
- Apply feature scaling
- Evaluate and optimize ML models
- Build an end-to-end ML application
- Deploy an ML model through a Flask REST API

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Flask
- CSV
- JSON
- REST API

---

## 📚 Projects

### 1. Student Information System

A Python-based console application that allows users to:

- Add students
- View students
- Search students
- Update student information
- Delete students

**Concepts:** Python, lists, dictionaries, functions, loops, conditions.

---

### 2. Student Data Processing System

A Python and NumPy project for processing student marks and calculating average values.

**Concepts:**

- Lists
- Dictionaries
- Functions
- NumPy
- Mean/Average

---

### 3. Full Data Preprocessing

A Pandas-based data preprocessing project.

The project demonstrates:

- Loading data
- Detecting missing values
- Handling missing values
- Removing duplicate records
- Selecting features
- Selecting target variables
- Data visualization

**Libraries:** Pandas, Matplotlib.

---

### 4. Student Prediction System

A supervised machine learning project that predicts student performance.

#### Regression

Predicts final marks using:

- Study Hours
- Attendance
- Assignment Score
- Previous Marks

Algorithm:

`Linear Regression`

Evaluation metrics:

- Mean Absolute Error
- R² Score

#### Classification

Predicts whether a student will pass or fail.

Algorithm:

`Logistic Regression`

Evaluation metric:

- Accuracy

---

### 5. Advanced ML Preparation

An unsupervised machine learning project using K-Means clustering.

The project includes:

- Feature engineering
- Standardization
- K-Means clustering
- Silhouette score
- Hyperparameter tuning
- Cluster comparison
- Cluster analysis

---

# 🚀 Final Capstone Project

## Student Performance Prediction System

The final project is an end-to-end machine learning application that predicts student performance based on academic and attendance-related features.

### Problem Statement

Educational institutions need ways to identify students who may underperform. This project uses machine learning to predict final marks and Pass/Fail status using historical student information.

### Input Features

- Study Hours
- Attendance
- Assignment Score
- Previous Marks

### Outputs

- Predicted Final Marks
- Predicted Pass/Fail Status

---

## 🧠 Machine Learning Models

### Regression

`LinearRegression`

Used to predict continuous final marks.

### Classification

`LogisticRegression`

Used to predict Pass/Fail status.

### Preprocessing

`StandardScaler`

Used for feature scaling.

---

## 🔄 ML Workflow

```text
Student Dataset
      ↓
Data Loading
      ↓
Data Preprocessing
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Feature Scaling
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Flask API
      ↓
JSON Prediction
```

---

## 🌐 Flask API

The final project exposes a REST API endpoint:

```text
POST /predict
```

Example request:

```json
{
    "study_hours": 6,
    "attendance": 85,
    "assignment_score": 70,
    "previous_marks": 72
}
```

Example response:

```json
{
    "predicted_marks": 76.5,
    "predicted_result": "PASS"
}
```

---

## 📂 Repository Structure

```text
ai-ml-internship-student-performance/
│
├── 01_python_fundamentals/
│   └── student_information_system.py
│
├── 02_numpy_data_processing/
│   └── student_data_processing.py
│
├── 03_pandas_preprocessing/
│   └── data_preprocessing.py
│
├── 04_supervised_learning/
│   └── student_prediction.py
│
├── 05_unsupervised_learning/
│   └── advanced_ml_preparation.py
│
├── 06_capstone_project/
│   ├── app.py
│   ├── student_data.csv
│   ├── requirements.txt
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-ml-internship-student-performance.git
```

Move into the project:

```bash
cd ai-ml-internship-student-performance
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run an individual project:

```bash
python 01_python_fundamentals/student_information_system.py
```

Run the final capstone:

```bash
cd 06_capstone_project
python app.py
```

The Flask server will run locally at:

```text
http://127.0.0.1:5000
```

---

## 📈 Learning Outcomes

Through this internship, I gained hands-on experience in:

- Python programming
- Data manipulation
- Data preprocessing
- Data visualization
- Feature engineering
- Feature scaling
- Supervised learning
- Unsupervised learning
- Regression
- Classification
- Clustering
- Model evaluation
- Hyperparameter tuning
- REST API development
- ML application deployment concepts

---

## 👨‍💻 Author

**B PAAWAN KUMAR**

B.Tech – Computer Science & Engineering (Software Engineering)

C.V. Raman Global University, Bhubaneswar

---

## ⭐ Acknowledgement

This repository contains the projects and practical work completed as part of my AI/ML Training & Internship.