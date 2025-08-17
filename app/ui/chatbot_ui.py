import streamlit as st
from app.ui.styles import REG_CSS

def chatbot_ui():
    st.markdown(REG_CSS, unsafe_allow_html=True)

    # Initialize session states
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "interview_started" not in st.session_state:
        st.session_state.interview_started = False

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
        if candidate_data:
            cd = candidate_data
            # Simple candidate profile section with all info inside
            st.markdown("""
                <div style="
                    background: rgba(52, 73, 94, 0.8);
                    padding: 1.5rem;
                    border-radius: 1rem;
                    margin-bottom: 1.5rem;
                    border: 1px solid #3498db;
                ">
                    <h3 style="
                        color: #3498db; 
                        margin: 0 0 1rem 0; 
                        font-size: 1.1rem;
                        text-align: center;
                        font-weight: 600;
                    ">👤 Candidate Profile</h3>
                </div>
            """, unsafe_allow_html=True)
            
            # Display candidate info using Streamlit components
            st.markdown(f"**Name:** {cd.get('full_name', '')}")
            st.markdown(f"**Position:** {cd.get('desired_position', '')}")
            st.markdown(f"**Experience:** {cd.get('years_experience', '')} years")
            st.markdown(f"**Location:** {cd.get('current_location', '')}")
            st.markdown(f"**Tech Stack:** {cd.get('tech_stack', '')}")
            st.markdown(f"**Email:** {cd.get('email', '')}")
            st.markdown(f"**Phone:** {cd.get('phone', '')}")
            
            # End interview button
            if st.button("🔚 End Interview", type="secondary", use_container_width=True):
                st.session_state.interview_started = False
                st.session_state.messages = []
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

    # Start Interview button (inline, no gap)
    if not st.session_state.interview_started:
        start_col = st.container()
        with start_col:
            # st.markdown("""
            #     <div style="
            #         background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
            #         padding: 2rem;
            #         border-radius: 1.5rem;
            #         text-align: center;
            #         box-shadow: 0 8px 32px rgba(0, 184, 148, 0.3);
            #         border: 1px solid rgba(255,255,255,0.1);
            #         margin: 2rem 0;
            #     ">
            #         <h2 style="
            #             color: white; 
            #             margin-bottom: 1rem;
            #             font-size: 1.8rem;
            #             text-shadow: 0 2px 4px rgba(0,0,0,0.3);
            #         ">🎯 Ready to Start?</h2>
            #         <p style="
            #             color: rgba(255,255,255,0.9); 
            #             margin-bottom: 1.5rem;
            #             font-size: 1.1rem;
            #         ">Click the button below to begin your technical interview</p>
            #     </div>
            # """, unsafe_allow_html=True)
            
            if st.button("🚀 Start Interview", type="primary", use_container_width=True):
                st.session_state.interview_started = True
                st.rerun()
        return  # stop rendering below until started

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

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        exit_keywords = ["exit", "quit", "end interview", "stop"]
        if any(keyword in prompt.lower() for keyword in exit_keywords):
            st.session_state.interview_started = False
            st.session_state.messages = []
            st.rerun()
            return

        st.session_state.messages.append({"role": "user", "content": prompt})
        ai_response = (
            f"I understand you said: '{prompt}'. "
            "This is a simulated response. In real implementation, "
            "this connects to the LLM for technical questions & feedback."
        )
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
