import streamlit as st
from textwrap import dedent
from app.ui.styles import REG_CSS
from app.services.llm_service import LLMService

def chatbot_ui():
    st.markdown(REG_CSS, unsafe_allow_html=True)

    # Initialize session states
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False
    if "is_generating_question" not in st.session_state:
        st.session_state.is_generating_question = False
    if "interview_completed" not in st.session_state:
        st.session_state.interview_completed = False
    if "final_report" not in st.session_state:
        st.session_state.final_report = ""
    if "asked_questions_global" not in st.session_state:
        st.session_state.asked_questions_global = []

    # Sidebar
    with st.sidebar:
        # Beautiful sidebar header with gradient
        st.markdown("""
            <div style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 2rem 1rem;
                border-radius: 1rem;
                margin: -1rem -1rem 2rem -1rem;
                text-align: center;
                box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            ">
                <h1 style="
                    color: white; 
                    font-size: 2rem; 
                    margin: 0; 
                    font-weight: 700;
                    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
                ">🚀 TalentScout</h1>
                <p style="
                    color: rgba(255,255,255,0.9); 
                    margin: 0.5rem 0 0 0; 
                    font-size: 0.9rem;
                ">AI-Powered Technical Interviews</p>
            </div>
        """, unsafe_allow_html=True)
        
        candidate_data = st.session_state.get("candidate_data")
        question_count = st.session_state.get("question_count", 0)
        if candidate_data:
            cd = candidate_data
            # Simple candidate profile section with all info inside
            st.markdown("""
        <div style="
            background: rgba(52, 73, 94, 0.8);
            padding: 0.5rem; 
            border-radius: 1rem;
            margin-bottom: 1.5rem;
            border: 1px solid #3498db;
            display: flex;
            align-items: center;
            justify-content: center;
        ">
            <h3 style="
                color: #3498db; 
                margin: 0; 
                font-size: 1.1rem;
                font-weight: 600;
            ">👤 Candidate Profile</h3>
        </div>
    """, unsafe_allow_html=True)

            # Polished candidate profile card with structured alignment
            email_value = cd.get('email', '') or ''
            email_html = f'<a href="mailto:{email_value}" style="color:#3498db; text-decoration:underline;">{email_value}</a>' if email_value else ''
            rows = [
                ("Name", cd.get('full_name','')),
                ("Position", cd.get('desired_position','')),
                ("Experience", f"{cd.get('years_experience','')} years"),
                ("Location", cd.get('current_location','')),
                ("Tech Stack", cd.get('tech_stack','')),
                ("Email", email_html),
                ("Phone", cd.get('phone','')),
            ]
            if st.session_state.interview_started:
                pv = min(question_count, 5)
                rows.append(("Question", f"{pv} / 5"))
            row_html = "".join(
                [
                    f'<div style="color:#bdc3c7; font-weight:600;">{label}</div>'
                    f'<div style="color:#ecf0f1;">{value}</div>'
                    for label, value in rows
                ]
            )
            profile_html = (
                '<div style="background: rgba(52, 73, 94, 0.6); padding: 0.8rem 1rem; border-radius: 0.8rem; border: 1px solid #2c3e50;">'
                '<div style="display:grid; grid-template-columns: 120px 1fr; column-gap: 0.75rem; row-gap: 0.35rem; align-items:start;">'
                f"{row_html}"
                '</div>'
                '</div>'
            )
            st.markdown(profile_html, unsafe_allow_html=True)
            # Display question count with progress representation
            if st.session_state.interview_started:
                progress_value = min(question_count, 5)
                progress_percent = int((progress_value / 5) * 100)
                st.markdown(f"""
                    <div style="margin-top: 0.2rem;">
                        <div style="
                            background: rgba(255,255,255,0.15);
                            border-radius: 999px;
                            overflow: hidden;
                            height: 10px;
                            border: 1px solid rgba(52,152,219,0.5);
                        ">
                            <div style="
                                width: {progress_percent}%;
                                background: linear-gradient(90deg, #3498db, #2ecc71);
                                height: 100%;
                                transition: width 300ms ease;
                            "></div>
                        </div>
                        <div style="color:#bdc3c7; font-size:0.8rem; margin-top:0.3rem; text-align:right;">{progress_value}/5</div>
                    </div>
                """, unsafe_allow_html=True)
            # End interview button
            if st.button("🔚 End Interview", type="secondary", use_container_width=True):
                st.session_state.interview_started = False
                st.session_state.messages = []
                st.session_state.interview_questions = []
                st.session_state.interview_scores = []
                st.session_state.used_skills = []
                st.session_state.current_question = None
                st.session_state.question_count = 0
                st.session_state.awaiting_answer = False
                st.session_state.is_generating_question = False
                st.rerun()

    # Greeting + Instructions
    # Simple greeting section
    st.markdown(f"""
        <div style="
            text-align: center;
            margin: 2rem 0 3rem 0;
            padding: 0 1rem;
        ">
            <h1 style="
                color: #e0e6ed; 
                font-size: 2.8rem; 
                margin-bottom: 1rem;
                font-weight: 600;
                letter-spacing: -0.5px;
            ">
                Hello {st.session_state["candidate_data"]["full_name"]}! 👋
            </h1>
            <p style="
                color: #b0b8c1; 
                font-size: 1.3rem; 
                margin: 0;
                font-weight: 400;
                line-height: 1.5;
            ">
                I'm your AI-powered technical interview assistant for the 
                <span style="color: #3498db; font-weight: 600;">{st.session_state["candidate_data"]["desired_position"]}</span> position.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Instructions section
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            padding: 2rem;
            border-radius: 1.5rem;
            margin: 0 auto 1rem auto; 
            width: 100%;
            border: 1px solid #3498db;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        ">
            <h3 style="
                color: #3498db; 
                margin-bottom: 1.5rem; 
                font-size: 1.4rem;
                text-align: center;
                border-bottom: 2px solid #3498db;
                padding-bottom: 0.8rem;
            ">🎯 What I'll do:</h3>
            <ul style="
                color: #ecf0f1; 
                font-size: 1.1rem; 
                text-align: left; 
                margin: 0; 
                padding-left: 2rem;
                line-height: 1.8;
            ">
                <li style="margin-bottom: 0.8rem;">✨ Ask technical questions based on your {st.session_state["candidate_data"]["years_experience"]} years of experience</li>
                <li style="margin-bottom: 0.8rem;">🛠️ Focus on your tech stack: <strong style="color: #f39c12;">{st.session_state["candidate_data"]["tech_stack"]}</strong></li>
                <li style="margin-bottom: 0.8rem;">💡 Provide real-time feedback on your responses</li>
                <li style="margin-bottom: 0.8rem;">🔍 Ask follow-up questions to explore your knowledge</li>
                <li style="margin-bottom: 0.8rem;">🚀 Move to new topics once we've covered a subject thoroughly</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # End interview instructions
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            padding: 2rem;
            border-radius: 1.5rem;
            margin: 0 auto 1rem auto; 
            width: 100%;
            border: 1px solid #e74c3c;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        ">
            <h3 style="
                color: #e74c3c; 
                margin-bottom: 1.5rem; 
                font-size: 1.4rem;
                text-align: center;
                border-bottom: 2px solid #e74c3c;
                padding-bottom: 0.8rem;
            ">⏹️ To end the interview:</h3>
            <ul style="
                color: #ecf0f1; 
                font-size: 1.1rem; 
                text-align: left; 
                margin: 0; 
                padding-left: 2rem;
                line-height: 1.8;
            ">
                <li style="margin-bottom: 0.8rem;">🔘 Click the "End Interview" button in the sidebar, or</li>
                <li style="margin-bottom: 0.8rem;">⌨️ Type "exit", "quit", or "end interview" in the chat</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Let's begin section
    # st.markdown("""
    #     <div style="
    #         background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
    #         padding: 1.5rem;
    #         border-radius: 1rem;
    #         margin: 0 auto 1rem auto;
    #         text-align: center;
    #         box-shadow: 0 4px 20px rgba(243, 156, 18, 0.3);
    #     ">
    #         <p style="
    #             color: white; 
    #             font-size: 1.3rem; 
    #             font-weight: 700; 
    #             margin: 0;
    #             text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    #         ">
    #             🚀 Let's begin! What would you like to start with?
    #         </p>
    #     </div>
    # """, unsafe_allow_html=True)

    # Interview state management
    if "interview_questions" not in st.session_state:
        st.session_state.interview_questions = []
    if "interview_scores" not in st.session_state:
        st.session_state.interview_scores = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = None
    if "question_count" not in st.session_state:
        st.session_state.question_count = 0
    if "awaiting_answer" not in st.session_state:
        st.session_state.awaiting_answer = False
    if "used_skills" not in st.session_state:
        st.session_state.used_skills = []

    # Helper to extract only the question sentence from a possibly long LLM output
    def _extract_question_only(text: str) -> str:
        if not isinstance(text, str):
            return ""
        qmark_index = text.find("?")
        if qmark_index != -1:
            return text[: qmark_index + 1].strip()
        for line in text.splitlines():
            if line.strip():
                return line.strip()
        return text.strip()

    def _normalize_question(text: str) -> str:
        if not isinstance(text, str):
            return ""
        import re as _re
        normalized = text.lower().strip()
        normalized = _re.sub(r"\s+", " ", normalized)
        normalized = _re.sub(r"[^a-z0-9 ?]", "", normalized)
        return normalized

    # Generate a unique question by retrying a few times if duplicates occur
    def _generate_unique_question(llm, tech_stack_list, years_experience, avoid_list, polite: bool = False, prev_question: str | None = None, focus_skill: str | None = None) -> str:
        seen_raw = list(avoid_list or [])
        seen_norm = { _normalize_question(q) for q in (avoid_list or []) }
        last_q = ""
        for _ in range(3):
            try:
                if polite:
                    raw = llm.polite_next_question(
                        tech_stack_list,
                        years_experience,
                        prev_question or "",
                        avoid_questions=avoid_list,
                        focus_skill=focus_skill,
                    )
                else:
                    raw = llm.generate_technical_question(
                        tech_stack_list,
                        years_experience,
                        avoid_questions=avoid_list,
                        focus_skill=focus_skill,
                    )
                q = _extract_question_only(raw)
                last_q = q
                if q and _normalize_question(q) not in seen_norm:
                    return q
            except Exception:
                # fall through to return last_q or continue retry
                pass
        return last_q or "Error generating question"

    def _pick_next_skill(tech_stack_list):
        if not tech_stack_list:
            return None
        # Choose the first skill not used yet; if all used, reset rotation
        for skill in tech_stack_list:
            if skill not in st.session_state.used_skills:
                st.session_state.used_skills.append(skill)
                return skill
        st.session_state.used_skills = [tech_stack_list[0]]
        return tech_stack_list[0]

    # If we are generating the first question, show overlay and do the work here
    if st.session_state.is_generating_question and not st.session_state.interview_started:
        st.markdown(
            """
            <div style="
                position: fixed; top: 0; left: 0; right: 0; bottom: 0;
                backdrop-filter: blur(6px);
                background: rgba(0,0,0,0.4);
                z-index: 9999;
                display: flex; align-items: center; justify-content: center;
            ">
                <div style="text-align: center; color: #ecf0f1;">
                    <div style="
                        border: 4px solid rgba(255,255,255,0.2);
                        border-top: 4px solid #3498db;
                        border-radius: 50%; width: 48px; height: 48px;
                        animation: spin 1s linear infinite; margin: 0 auto;
                    "></div>
                    <p style="margin-top: 1rem; font-size: 1.1rem;">Preparing your first question...</p>
                </div>
            </div>
            <style>
                @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
            </style>
            """,
            unsafe_allow_html=True,
        )

        candidate_data = st.session_state.get("candidate_data", {})
        tech_stack = candidate_data.get("tech_stack", "")
        years_experience = candidate_data.get("years_experience", 0)
        if isinstance(tech_stack, str):
            tech_stack_list = [t.strip() for t in tech_stack.split(",") if t.strip()]
        else:
            tech_stack_list = tech_stack if tech_stack else []
        llm = LLMService()
        # Reset completion/report on fresh start
        st.session_state.interview_completed = False
        st.session_state.final_report = ""
        focus_skill = _pick_next_skill(tech_stack_list)
        question = _generate_unique_question(
            llm,
            tech_stack_list,
            years_experience,
            avoid_list=st.session_state.get("asked_questions_global", []),
            polite=False,
            focus_skill=focus_skill,
        )
        st.session_state.current_question = question
        st.session_state.messages.append({"role": "assistant", "content": question})
        # Track globally to reduce repeats across interviews
        if question and question not in st.session_state.asked_questions_global:
            st.session_state.asked_questions_global.append(question)
        st.session_state.awaiting_answer = True
        st.session_state.question_count = 1
        st.session_state.interview_started = True
        st.session_state.is_generating_question = False
        st.rerun()
        return

    if not st.session_state.interview_started:
        start_col = st.container()
        with start_col:
            if st.button("🚀 Start Interview", type="primary", use_container_width=True):
                # Reset completion/report on fresh start
                st.session_state.interview_completed = False
                st.session_state.final_report = ""
                # Reset per-interview state to avoid repetition
                st.session_state.messages = []
                st.session_state.interview_questions = []
                st.session_state.interview_scores = []
                st.session_state.used_skills = []
                st.session_state.current_question = None
                st.session_state.question_count = 0
                st.session_state.awaiting_answer = False
                st.session_state.is_generating_question = True
                st.rerun()
        # Show final report below Start Interview if available
        if st.session_state.get("interview_completed") and st.session_state.get("final_report"):
            st.markdown(
                f"""
                <div style="
                    margin-top: 1rem; padding: 1rem; border: 1px solid #3498db; border-radius: 0.75rem;
                    background: rgba(52, 73, 94, 0.6); color: #ecf0f1;
                ">
                    <h3 style="margin-top:0; color:#3498db;">📋 Interview Report</h3>
                    <div style="white-space: pre-wrap; line-height: 1.6;">{st.session_state.final_report}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        return

    # Interview loop: max 5 questions
    candidate_data = st.session_state.get("candidate_data", {})
    tech_stack = candidate_data.get("tech_stack", "")
    years_experience = candidate_data.get("years_experience", 0)
    if isinstance(tech_stack, str):
        tech_stack_list = [t.strip() for t in tech_stack.split(",") if t.strip()]
    else:
        tech_stack_list = tech_stack if tech_stack else []
    llm = LLMService()

    # Removed separate text input; answers are handled via chat_input below

    # ---------------- CHAT INTERFACE ---------------- #
    st.markdown('<div class="chat-container" style="margin-top:1rem;">', unsafe_allow_html=True)

    # Show messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-start; margin: 0.8rem 0;">
                    <div style="
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 1.2rem; 
                        padding: 1.2rem 1.5rem; 
                        max-width: 80%; 
                        border: none;
                        color: white;
                        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
                        position: relative;
                    ">
                        <div style="
                            position: absolute;
                            top: -8px;
                            left: 20px;
                            background: #667eea;
                            padding: 0.3rem 0.8rem;
                            border-radius: 1rem;
                            font-size: 0.7rem;
                            color: white;
                            font-weight: 600;
                        ">🤖 AI Assistant</div>
                        {message["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: flex-end; margin: 0.8rem 0;">
                    <div style="
                        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                        border-radius: 1.2rem; 
                        padding: 1.2rem 1.5rem; 
                        max-width: 80%; 
                        border: none;
                        color: white;
                        box-shadow: 0 4px 20px rgba(255, 107, 107, 0.3);
                        position: relative;
                    ">
                        <div style="
                            position: absolute;
                            top: -8px;
                            right: 20px;
                            background: #ff6b6b;
                            padding: 0.3rem 0.8rem;
                            border-radius: 1rem;
                            font-size: 0.7rem;
                            color: white;
                            font-weight: 600;
                        ">👤 You</div>
                        {message["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Chat input (disabled when interview is completed)
    if not st.session_state.get("interview_completed"):
        prompt = st.chat_input("Type your message here...")
    else:
        prompt = None

    if prompt:
        exit_keywords = ["exit", "quit", "end interview", "stop"]
        if any(keyword in prompt.lower() for keyword in exit_keywords):
            st.session_state.interview_started = False
            st.session_state.messages = []
            st.session_state.interview_questions = []
            st.session_state.interview_scores = []
            st.session_state.used_skills = []
            st.session_state.current_question = None
            st.session_state.question_count = 0
            st.session_state.awaiting_answer = False
            st.session_state.is_generating_question = False
            st.rerun()
            return

        st.session_state.messages.append({"role": "user", "content": prompt})
        # If we are awaiting an answer within the interview loop, evaluate and move forward
        if st.session_state.awaiting_answer and st.session_state.question_count <= 5:
            if prompt.strip():
                try:
                    eval_result = llm.evaluate_answer(
                        st.session_state.current_question,
                        prompt,
                        tech_stack_list,
                        years_experience
                    )
                    score = eval_result.get("score", 0)
                    feedback = eval_result.get("feedback", "")
                except Exception as e:
                    score = 0
                    feedback = f"Error evaluating answer: {str(e)}"
                st.session_state.interview_scores.append(score)
                st.session_state.interview_questions.append(st.session_state.current_question)
                ai_response = f"Score: {score}/5\nFeedback: {feedback}"
                st.session_state.messages.append({"role": "assistant", "content": ai_response.replace('\n', '<br/>')})
            # Next question or end
            if st.session_state.question_count < 5:
                avoid_list = (
                    st.session_state.interview_questions
                    + [st.session_state.current_question]
                    + st.session_state.get("asked_questions_global", [])
                )
                if not prompt.strip():
                    next_question = _generate_unique_question(
                        llm,
                        tech_stack_list,
                        years_experience,
                        avoid_list=avoid_list,
                        polite=True,
                        prev_question=st.session_state.current_question,
                        focus_skill=_pick_next_skill(tech_stack_list),
                    )
                else:
                    next_question = _generate_unique_question(
                        llm,
                        tech_stack_list,
                        years_experience,
                        avoid_list=avoid_list,
                        polite=False,
                        focus_skill=_pick_next_skill(tech_stack_list),
                    )
                st.session_state.current_question = next_question
                st.session_state.messages.append({"role": "assistant", "content": next_question})
                if next_question and next_question not in st.session_state.asked_questions_global:
                    st.session_state.asked_questions_global.append(next_question)
                st.session_state.question_count += 1
                st.session_state.awaiting_answer = True
            else:
                try:
                    report_body = llm.generate_report(
                        answers=[m["content"] for m in st.session_state.messages if m["role"] == "user"],
                        scores=st.session_state.interview_scores,
                        tech_stack=tech_stack_list,
                        experience=years_experience
                    )
                except Exception as e:
                    report_body = f"Error generating report: {str(e)}"
                scores = st.session_state.interview_scores
                overall = round(sum(scores) / len(scores), 2) if scores else 0.0
                st.session_state.final_report = f"{report_body}\n\nOverall Score: {overall}/5"
                # Inform completion and thanks in chat
                completion_msg = "All questions have been shown.\nThank you for attending interview Happy Learning."
                st.session_state.messages.append({"role": "assistant", "content": completion_msg.replace('\n', '<br/>')})
                st.session_state.awaiting_answer = False
                st.session_state.interview_completed = True
            st.rerun()
        else:
            # Generic chat response outside interview context
            ai_response = (
                f"I understand you said: '{prompt}'. "
                "This is a simulated response. In real implementation, "
                "this connects to the LLM for technical questions & feedback."
            )
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            st.rerun()

    # If interview completed, show only End Interview button instead of input field
    if st.session_state.get("interview_completed"):
        if st.button("🔚 End Interview", type="primary"):
            st.session_state.interview_started = False
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
