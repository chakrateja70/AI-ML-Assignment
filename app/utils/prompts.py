# Prompt for generating technical questions for a candidate's tech stack and experience
TECH_QUESTION_PROMPT = (
    "You are an expert technical interviewer. Given the following tech stack: {tech_stack} "
    "and {experience} years of experience, generate {num_questions} relevant and challenging technical interview questions "
    "to assess proficiency. Tailor the questions to the candidate's experience level. "
    "Questions should be clear, concise, and cover different aspects of the technologies mentioned. "
    "Return only the questions as a numbered list."
)

# Prompt for generating a single technical question
TECH_QUESTION_SINGLE_PROMPT = (
    "You are an expert technical interviewer. Given the following tech stack: {tech_stack} "
    "and {experience} years of experience, generate one relevant and challenging technical interview question. "
    "Tailor the question to the candidate's experience level. Return only the question."
)

# Prompt for evaluating candidate's answer
EVALUATE_ANSWER_PROMPT = (
    "You are an expert technical interviewer. Given the question: {question}, the candidate's answer: {answer}, "
    "tech stack: {tech_stack}, and {experience} years of experience, evaluate the answer and provide a score from 0 to 5. "
    "Also provide brief feedback. Format: 'Score: X\nFeedback: ...'"
)

# Prompt for politely handling no answer and asking another question
POLITE_NEXT_QUESTION_PROMPT = (
    "The candidate did not answer the previous question: '{prev_question}'. "
    "Politely acknowledge and ask another relevant technical question based on tech stack: {tech_stack} and experience: {experience}. "
    "Return only the new question."
)

# Prompt for generating final report and polite closing
FINAL_REPORT_PROMPT = (
    "You are an expert technical interviewer. Given the candidate's answers: {answers}, scores: {scores}, "
    "tech stack: {tech_stack}, and experience: {experience}, generate a concise 4-5 line report summarizing their performance. "
    "End with: 'Thank you for attending interview, Happy Learning.'"
)
