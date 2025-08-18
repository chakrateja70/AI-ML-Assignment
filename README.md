## TalentScout - AI-Powered Technical Interview Assistant

TalentScout is a Streamlit app that conducts short, AI-powered technical interviews. It generates tailored questions from a candidate’s tech stack and experience, evaluates answers with concise feedback, and produces a brief interview summary.

### Features
- Tailored technical questions based on skills and experience
- Live scoring (0–5) and actionable feedback per answer
- Polite handling when the candidate skips answers
- 5-question interview loop and a concise final report
- Candidate registration with persistence in MySQL

### Tech Stack
- Python, Streamlit
- MySQL (mysql-connector-python) for simple persistence
- SQLAlchemy (async engine scaffolded)
- Groq LLM API via `groq` and `langchain` for prompts

---

## Quick Start

1) Clone and enter the project directory
```bash
git clone https://github.com/chakrateja70/AI-ML-Assignment.git
cd AI-ML-Assignment
```

2) Create a virtual environment and install dependencies
```bash
python -m venv .venv
. .venv/Scripts/activate  # on Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3) Create a `.env` file in the project root
```bash
copy NUL .env  # Windows
```
Then add the following variables (edit values as needed):
```env
# Groq API
GROQ_API_KEY=your_groq_api_key_here

# MySQL connection
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=talentscout
```

4) Prepare the MySQL database/table
```sql
CREATE DATABASE IF NOT EXISTS talentscout;
USE talentscout;

CREATE TABLE IF NOT EXISTS candidate_info (
  id INT PRIMARY KEY AUTO_INCREMENT,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone VARCHAR(20) NOT NULL,
  years_experience INT NOT NULL,
  desired_position VARCHAR(100) NOT NULL,
  current_location VARCHAR(100) NOT NULL,
  tech_stack VARCHAR(255) NOT NULL
);
```

5) Run the app
```bash
streamlit run app.py
```

---

## How to Use
1) Open the Streamlit URL shown in the terminal (usually `http://localhost:8501`).
2) Fill out the Candidate Registration form and submit.
3) Click “Start Interview” to begin.
4) Answer questions in the chat. You’ll receive a score and short feedback after each.
5) After 5 questions, a brief final report appears. You can end the interview anytime from the sidebar or by typing “end interview”.

---

## Configuration Details

### Environment Variables
The app loads environment variables via `python-dotenv`.
- `GROQ_API_KEY`: Required to call the Groq LLM.
- `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_HOST`, `MYSQL_PORT`, `MYSQL_DATABASE`: MySQL connection settings used by `app.utils.helpers.insert_candidate_data` via `app.db.mysql.get_db_connection`.

### LLM Model
`app/services/llm_service.py` defaults to:
```
meta-llama/llama-4-scout-17b-16e-instruct
```
You can override by passing a different model name when instantiating `LLMService`.

---