## TalentScout - AI-Powered Technical Interview Assistant

### Project Overview
TalentScout is a Streamlit-based hiring assistant that conducts short, AI-powered technical interviews. It:
- Generates questions tailored to a candidate’s tech stack and experience
- Scores answers (0–5) with concise, actionable feedback
- Handles skipped answers politely and avoids repeating questions
- Produces a brief final summary report after a 5-question loop
- Saves candidate profiles to MySQL before starting the interview

### Installation Instructions
1) Clone and enter the project directory
```bash
git clone https://github.com/chakrateja70/AI-ML-Assignment.git
cd AI-ML-Assignment
```

2) Create a virtual environment and install dependencies
```bash
python -m venv venv #create virtual env
venv/Scripts/activate #activate venv
pip install -r requirements.txt
```

3) Create a `.env` file in the project root and add:
```env
# Groq API
GROQ_API_KEY=your_groq_api_key_here

# MySQL connection
MYSQL_USER = user_name
MYSQL_PASSWORD = your_password
MYSQL_HOST = host_name
MYSQL_PORT = port_number
MYSQL_DATABASE = talentscout
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

Note: The interview will only start if the candidate record is successfully saved in MySQL.

### Usage Guide
1) Open `http://localhost:8501`.
2) Complete the Candidate Registration form and submit.
3) Click “Start Interview”.
4) Answer each question in the chat to receive a score and feedback.
5) After 5 questions, view the final report; end anytime via the sidebar button or by typing “end interview”.

### Technical Details
- Libraries: `streamlit`, `sqlalchemy`, `mysql-connector-python`, `aiomysql`, `python-dotenv`, `groq`, `langchain`.
- Model: Groq chat completions with default `meta-llama/llama-4-scout-17b-16e-instruct` (see `app/services/llm_service.py`).
- Architecture:
  - `app.py` → entry point (`streamlit run app.py`).
  - `app/main.py` routes between `candidate_form` and `chatbot_ui` using session state.
  - `app/ui/candidate_form.py` validates data and inserts into MySQL via `app/utils/helpers.py`.
  - `app/ui/chatbot_ui.py` manages interview flow, messages, and UI polish.
  - `app/services/llm_service.py` wraps Groq calls for question generation, answer evaluation, and final report.
  - `app/utils/prompts.py` holds prompt templates.
  - `app/db/mysql.py` loads `.env` and provides a direct MySQL connection (plus an async SQLAlchemy engine scaffold).
  - `app/ui/styles.py` injects CSS for a dark, modern UI.
- Decisions:
  - Streamlit for rapid UI + stateful chat.
  - Direct MySQL insert with `mysql-connector-python` (simple persistence); async SQLAlchemy left as future-ready.
  - Clear module boundaries: UI, LLM service, prompts, and DB utilities.

### Prompt Design
- Single question generation (`TECH_QUESTION_SINGLE_PROMPT`):
  - Maps experience to difficulty (0→basic, 1–3→moderate, 4–10→upper-moderate, 11+→hard).
  - Focuses on one `focus_skill` at a time; includes an `avoid_questions` list to reduce repetition.
  - Enforces output as exactly one question line with no preface.
- Polite no-answer (`POLITE_NEXT_QUESTION_PROMPT`):
  - Regenerates one standalone question without referencing previous context; still respects difficulty and `avoid_questions`.
- Answer evaluation (`EVALUATE_ANSWER_PROMPT`):
  - Strict 2-line output: `Score: <0-5>` and `Feedback: <1-3 short lines>`.
- Final report (`FINAL_REPORT_PROMPT`):
  - 3–5 lines summarizing strengths/weaknesses; score added by app, not the model.
- Post-processing safeguards:
  - `_extract_question_only` trims extra content to the first sentence/question mark.
  - Score clamped to 0–5; feedback trimmed to max 3 lines.
  - `used_skills` rotation ensures coverage across the provided tech stack.

### Challenges & Solutions
- Avoiding duplicate/related questions
  - Solution: Maintain `avoid_questions`, rotate `focus_skill`, and post-process to extract only the question. Fallback retries used for uniqueness.
- Robustly parsing LLM output
  - Solution: Enforce strict prompt formats; parse only `Score:`/`Feedback:` lines, clamp values, and trim feedback length.
- Handling skipped/empty answers gracefully
  - Solution: Provide a polite alternative question path without penalizing or referencing previous context.
- Preventing database duplicates and failures from blocking UX
  - Solution: Use `INSERT IGNORE` on `email` unique constraint; show clear error if insert fails; gate interview start on successful save.
- Managing Streamlit state and responsiveness
  - Solution: Use session flags (`is_generating_question`, `awaiting_answer`, `interview_started`) and a lightweight overlay during first question generation.