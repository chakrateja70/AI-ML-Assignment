TECH_QUESTION_PROMPT = (
    """You are an experienced technical interviewer conducting a real interview. Generate {num_questions} practical interview questions 
    for a candidate with {experience} years of experience in: {tech_stack}.
    
    DIFFICULTY MAPPING (EXPERIENCE-BASED):
    - 0-1 years → basic: "What is...", "Define...", "Name three..." (ONE concept per question, no compound questions)
    - 2-3 years → moderate: "How would you handle...", "What's your approach to...", "Describe a scenario where..."
    - 4-10 years → upper-moderate: "How would you design...", "What are the trade-offs of...", "How would you optimize..."
    - 11+ years → hard: "How would you architect...", "What's your strategy for...", "How would you lead a team to..."
    
    QUESTION TYPES TO FOCUS ON:
    - For 0-1 years: Single concept definitions (what is X?, define Y, name three types of Z)
    - For 2+ years: Problem-solving approaches, experience-based scenarios, decision-making
    - Best practices and troubleshooting (for experienced candidates only)
    
    OUTPUT RULES (MANDATORY):
    - Each question on its own line
    - No numbering, bullets, or prefixes
    - Questions should feel like a real interviewer is asking
    - Focus on verbal explanations, not coding
    
    Generate {num_questions} {difficulty_label} interview questions:
    """
)

TECH_QUESTION_SINGLE_PROMPT = (
    """You are conducting a technical interview. Ask EXACTLY ONE {difficulty_label} question 
    for a candidate with {experience} years of experience in: {tech_stack}.
    
    FOCUS AREA: {focus_skill} (ask specifically about this technology/concept)
    
    QUESTION STYLES BY EXPERIENCE:
    - basic (0-1 years): "What is...", "Define...", "Name..." (Single concept only, no compound questions)
    - moderate: "How do you handle...", "Describe your approach to...", "What would you do if..."
    - upper-moderate: "How would you design...", "What are the trade-offs...", "How do you optimize..."
    - hard: "How would you architect...", "What's your strategy...", "How do you mentor others on..."
    
    AVOID THESE PREVIOUSLY ASKED QUESTIONS:
    {avoid_questions}
    
    REQUIREMENTS:
    - Ask like a real interviewer would
    - For 0-1 years: ONE simple, direct question about ONE concept only
    - For 2+ years: Focus on explanation/discussion, not coding
    - Should take 30 seconds to 1 minute to answer for beginners, 1-2 minutes for experienced
    - Must be specific to the focus skill mentioned
    
    OUTPUT: Just the interview question, no labels or formatting.
    """
)

EVALUATE_ANSWER_PROMPT = (
    """You are evaluating a candidate's interview response as a technical interviewer.
    
    INTERVIEW CONTEXT:
    Question Asked: {question}
    Candidate's Answer: {answer}
    Tech Stack: {tech_stack} | Experience: {experience} years
    
    SCORING SCALE (0-5):
    5 = Excellent: Comprehensive understanding, mentions best practices, real-world insights
    4 = Good: Solid understanding, mostly accurate, good practical knowledge
    3 = Average: Basic understanding, some gaps but shows general knowledge
    2 = Below Average: Limited understanding, several inaccuracies or missing key points
    1 = Poor: Significant gaps, major misunderstandings
    0 = No answer or completely wrong
    
    EVALUATION FOCUS:
    - Accuracy of technical knowledge
    - Depth of understanding for their experience level
    - Practical application awareness
    - Communication clarity
    
    OUTPUT FORMAT (EXACT):
    Score: <0-5>
    Feedback: <Brief, constructive feedback in 1-2 sentences, max 150 characters>
    
    EXAMPLE:
    Score: 3
    Feedback: Good basic understanding but missed key performance considerations. Explain caching strategies next time.
    
    Evaluate this interview response:
    """
)

POLITE_NEXT_QUESTION_PROMPT = (
    """Continue the technical interview. Ask EXACTLY ONE {difficulty_label} question 
    for a candidate with {experience} years of experience in: {tech_stack}.
    
    FOCUS ON: {focus_skill}
    
    PREVIOUSLY COVERED (don't repeat):
    {avoid_questions}
    
    INTERVIEW STYLE:
    - Ask naturally like an interviewer would
    - Focus on discussion/explanation questions
    - Appropriate difficulty for {experience} years experience
    - Should be answerable in 1-2 minutes verbally
    
    OUTPUT: Just ask the next interview question directly.
    """
)

# FINAL_REPORT_PROMPT = (
#     """Provide a final technical interview assessment for this candidate.
    
#     INTERVIEW PERFORMANCE:
#     Candidate Answers: {answers}
#     Question Scores: {scores}
#     Tech Stack: {tech_stack} | Experience: {experience} years
    
#     ASSESSMENT AREAS:
#     1. Technical Knowledge Strength
#     2. Areas Needing Improvement  
#     3. Communication Skills
#     4. Experience Level Appropriateness
#     5. Hiring Recommendation
    
#     TONE: Professional interviewer providing constructive feedback
    
#     FORMAT: 4-5 sentences covering:
#     - What they did well technically
#     - Key areas to improve
#     - Overall communication/interview performance
#     - Recommendation (hire/not hire/needs development)
#     - Encouraging closing
    
#     EXAMPLE:
#     The candidate demonstrated solid foundational knowledge in React and JavaScript fundamentals. 
#     However, they need to strengthen their understanding of state management and component lifecycle concepts. 
#     Communication was clear and they showed good problem-solving thinking during responses. 
#     Recommend for junior developer role with mentorship on advanced React patterns. 
#     Thank you for your time today, and best of luck with your continued learning!
    
#     Generate interview assessment:
#     """
# )

FINAL_REPORT_PROMPT = (
    """Generate a comprehensive technical interview assessment based on the candidate's performance.
    
    PERFORMANCE DATA:
    Candidate Responses: {answers}
    Question Scores: {scores}
    Tech Stack: {tech_stack} | Experience Level: {experience} years
    
    REPORT STRUCTURE REQUIREMENTS:
    1. Technical Strengths (specific skills demonstrated)
    2. Areas for Improvement (specific gaps identified)
    3. Communication and Problem-Solving Assessment
    4. Recommendation for role suitability
    5. Growth potential and next steps
    
    WRITING GUIDELINES:
    - Be specific and evidence-based
    - Reference actual performance on questions
    - Consider experience level expectations
    - Provide constructive, actionable feedback
    - Maintain professional, encouraging tone
    
    LENGTH: 4-6 concise sentences covering all key aspects
    
    EXAMPLE FORMAT:
    Candidate demonstrated solid foundational knowledge in Python with particularly strong understanding of data structures and OOP concepts. 
    Areas for improvement include async programming patterns and performance optimization techniques. 
    Communication was clear with good problem-solving approach, though explanations could be more detailed. 
    Suitable for mid-level developer role with mentorship in advanced topics. 
    Recommend focusing on practical projects involving concurrency and system design.
    Thank you for your time. Best of luck with your continued learning journey.
    
    Generate assessment report:
    """
)