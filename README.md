# UN Votes Analyzer

A full-stack data engineering and analytics platform that analyzes United Nations General Assembly voting patterns to uncover geopolitical insights.

---

## Features

* Country stance analysis by issue
* Country-to-country alignment scoring
* Global voting distribution
* Interactive dashboard (React)
* FastAPI backend with real-time queries

---

## Architecture

```
UN Dataset → ETL Pipeline → PostgreSQL → Analytics Engine → FastAPI → React Dashboard
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Pandas
* SQLAlchemy
* PostgreSQL

### Frontend

* React (Vite)
* Recharts
* Axios

---

## Setup Instructions

### 1. Clone repo

```bash
git clone https://github.com/YOUR_USERNAME/un-votes-analyser.git
cd un-votes-analyser
```

---

### 2. Backend setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Run pipeline

```bash
python -m scripts.run_pipeline
```

---

### 4. Run API

```bash
uvicorn src.api.main:app --reload
```

---

### 5. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

---

## Example API Endpoints

* `/country/India`
* `/compare/India/United States`
* `/global/NUCLEAR`

---

## Key Insights

* Identifies geopolitical voting patterns
* Measures alignment between countries
* Tracks issue-based behavior

---

## Future Enhancements

* Voting blocs clustering
* Time-series analysis
* AI-generated insights
* Advanced visualizations

---

## Author
Navya Nawal
Built as a flagship Data Engineering project.
