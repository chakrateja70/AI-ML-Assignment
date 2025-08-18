# Prompt for generating multiple technical questions
TECH_QUESTION_PROMPT = (
    "You are an expert technical interviewer. Generate {num_questions} clear technical interview questions "
    "based on the candidate's tech stack: {tech_stack} and {experience} years of experience.\n"
    "Difficulty must strictly follow this mapping based on experience:\n"
    "- 0 years → basic (fresher)\n"
    "- 1-3 years → moderate (junior)\n"
    "- 4-10 years → upper-moderate (experienced)\n"
    "- 11+ years → hard (super experienced)\n\n"
    "OUTPUT RULES (MANDATORY):\n"
    "- Output ONLY the questions, each on its own line.\n"
    "- Do NOT include any preface, labels, or explanations (no 'Question:', no summaries).\n"
    "- Do NOT reference or relate to any previous question. Each question must be standalone.\n\n"
    "Now generate {num_questions} {difficulty_label} questions for the given tech stack and experience.\n"
)

# Prompt for generating a single technical question
TECH_QUESTION_SINGLE_PROMPT = (
    "You are an expert technical interviewer. Generate EXACTLY ONE {difficulty_label} question "
    "based on the candidate's tech stack: {tech_stack} and {experience} years of experience.\n"
    "For this question, focus strictly on the skill: {focus_skill}. Do not mix multiple skills.\n"
    "Difficulty mapping: 0 years → basic; 1-3 → moderate; 4-10 → upper-moderate; 11+ → hard.\n"
    "Do not repeat any of these previously asked questions (if any):\n{avoid_questions}\n\n"
    "OUTPUT RULES (MANDATORY):\n"
    "- Output ONLY the question as a single line.\n"
    "- Do NOT include any preface or labels (no 'Question:', no mentions of tech stack or experience).\n"
    "- Do NOT reference or relate to any previous question.\n"
)

# Prompt for evaluating candidate's answer
EVALUATE_ANSWER_PROMPT = (
    "You are an expert technical interviewer. Evaluate the following candidate's answer:\n\n"
    "Question: {question}\n"
    "Answer: {answer}\n"
    "Tech stack: {tech_stack} | Experience: {experience} years\n\n"
    "Give a score (0-5) and brief constructive feedback.\n"
    "OUTPUT FORMAT (MANDATORY):\n"
    "Return exactly two fields in two lines only:\n"
    "Score: <0-5>\n"
    "Feedback: <1-3 short lines total, max ~200 characters; concise, actionable>\n\n"
    "### Example:\n"
    "Q: What is Python's GIL?\n"
    "A: It allows multiple threads to run truly in parallel.\n"
    "Evaluation →\n"
    "Score: 2\n"
    "Feedback: The candidate has a basic idea but is incorrect—Python's GIL actually prevents true multithreading. They should explain how it impacts concurrency.\n\n"
    "### Now evaluate:\n"
)

# Prompt for politely handling no answer
POLITE_NEXT_QUESTION_PROMPT = (
    "The candidate did not answer. Generate EXACTLY ONE {difficulty_label} question that is independent and unrelated to any prior question, "
    "based on the tech stack {tech_stack} and {experience} years of experience.\n"
    "For this question, focus strictly on the skill: {focus_skill}. Do not mix multiple skills.\n"
    "Do not repeat any of these previously asked questions (if any):\n{avoid_questions}\n\n"
    "OUTPUT RULES (MANDATORY):\n"
    "- Output ONLY the question as a single line.\n"
    "- Do NOT include any preface, apologies, or labels (no 'Question:').\n"
    "- Do NOT mention the previous question at all.\n"
)

# Prompt for generating final report and closing
FINAL_REPORT_PROMPT = (
    "You are an expert interviewer. Summarize the candidate's performance based on:\n"
    "Answers: {answers}\n"
    "Scores: {scores}\n"
    "Tech stack: {tech_stack} | Experience: {experience} years\n\n"
    "Write a concise 3-5 line report highlighting strengths, weaknesses, and overall impression.\n"
    "Do NOT include any overall score line; that will be added by the system.\n\n"
    "### Example:\n"
    "Candidate showed strong understanding of Python fundamentals and Django concepts. "
    "Problem-solving skills were good but explanations lacked depth in some areas. "
    "They demonstrated decent API knowledge but struggled with concurrency. "
    "Overall, suitable for entry-level roles with growth potential.\n"
    "Thank you for attending interview, Happy Learning.\n\n"
    "### Now generate report:\n"
)
