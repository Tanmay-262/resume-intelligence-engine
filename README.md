# 🚀 AI-Powered Resume Parser & Candidate Ranking System

An intelligent Resume Screening and Candidate Ranking System that automatically extracts information from resumes, analyzes candidate skills, matches them against job descriptions, and ranks applicants based on relevance using Natural Language Processing (NLP) and Machine Learning techniques.

---

## 📌 Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually screening each resume is time-consuming and inefficient.

This project automates the recruitment process by:

* Extracting candidate details from PDF resumes
* Identifying technical and professional skills
* Matching resumes with job descriptions
* Calculating candidate-job fit scores
* Ranking candidates based on relevance
* Providing an efficient hiring workflow

---

## ✨ Features

### 📄 Resume Parsing

* Extract candidate name
* Extract email address
* Extract phone number
* Extract education details
* Extract technical skills

### 🎯 Job Description Matching

* Upload a job description
* Compare candidate profiles with requirements
* Calculate similarity scores

### 📊 Candidate Ranking

* Rank multiple resumes automatically
* Display top candidates
* Generate recruitment insights

### 🧠 Semantic Search

* Understand context beyond keyword matching
* Match similar skills and technologies
* Improve screening accuracy

### 🔍 Resume Database Search

* Store resume embeddings
* Retrieve relevant candidates instantly
* Vector-based similarity search

---

## 🏗️ System Architecture

```text
Resume PDF
     │
     ▼
PDF Text Extraction
     │
     ▼
NLP Processing
     │
     ├── Candidate Information Extraction
     ├── Skill Identification
     └── Education Parsing
     │
     ▼
Embedding Generation
     │
     ▼
Similarity Calculation
     │
     ▼
Candidate Ranking
     │
     ▼
Dashboard / API Output
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning & NLP

* Scikit-Learn
* spaCy
* Sentence Transformers
* Transformers

### Data Processing

* Pandas
* NumPy

### PDF Processing

* pdfplumber
* PyPDF2

### Vector Database

* FAISS

### Backend

* FastAPI

### Frontend

* Streamlit

### Deployment

* Docker

---

## 📂 Project Structure

```text
resume-parser-ai/
│
├── data/
│   ├── resumes/
│   └── job_descriptions/
│
├── models/
│
├── src/
│   ├── parser.py
│   ├── extractor.py
│   ├── ranker.py
│   ├── embeddings.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── Dockerfile
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-parser-ai.git
cd resume-parser-ai
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### Streamlit Application

```bash
streamlit run app.py
```

### FastAPI Server

```bash
uvicorn app:app --reload
```

---

## 📈 Machine Learning Pipeline

### Step 1

Extract text from PDF resumes.

### Step 2

Clean and preprocess text.

### Step 3

Identify candidate information using NLP.

### Step 4

Generate sentence embeddings.

### Step 5

Convert job descriptions into embeddings.

### Step 6

Calculate similarity scores.

### Step 7

Rank candidates based on relevance.

---

## 📊 Evaluation Metrics

* Cosine Similarity
* Precision
* Recall
* F1 Score
* Ranking Accuracy

---

## 🔮 Future Enhancements

* Multi-language resume parsing
* AI interview question generation
* Candidate skill gap analysis
* LLM-powered resume feedback
* ATS compatibility scoring
* Recruiter analytics dashboard
* Cloud deployment on AWS

---

## 💼 Real-World Applications

* Recruitment Agencies
* HR Departments
* Talent Acquisition Teams
* Job Portals
* Staffing Companies

---

## 🧪 Sample Output

```json
{
  "candidate_name": "Tanmay Jain",
  "email": "tanmay@example.com",
  "skills": [
    "Python",
    "Machine Learning",
    "NLP",
    "SQL"
  ],
  "match_score": 92.4
}
```

---

## 📚 Key Skills Demonstrated

* Natural Language Processing (NLP)
* Information Extraction
* Resume Parsing
* Semantic Search
* Machine Learning
* Candidate Ranking
* Vector Databases
* FastAPI Development
* Streamlit Deployment
* MLOps Fundamentals

---

## 👨‍💻 Author

**Tanmay Jain**

B.Tech Computer Science Engineering
Aspiring AI/ML Engineer | Machine Learning | NLP | Generative AI | Agentic AI

---

⭐ If you found this project useful, consider giving it a star!
