import streamlit as st
from app.utils.helpers import validate_candidate_data, insert_candidate_data
from app.ui.styles import REG_CSS

def candidate_form():
    st.markdown(REG_CSS, unsafe_allow_html=True)
    
    # Simple header section
    st.markdown("""
        <div style="
            text-align: center;
            margin: 2rem 0 3rem 0;
            padding: 0 1rem;
        ">
            <h1 style="
                color: #e0e6ed; 
                font-size: 2.5rem; 
                margin-bottom: 1rem;
                font-weight: 600;
                letter-spacing: -0.5px;
            ">🚀 TalentScout</h1>
            <p style="
                color: #b0b8c1; 
                font-size: 1.2rem; 
                margin: 0 0 1.5rem 0;
                font-weight: 400;
                line-height: 1.5;
            ">AI-Powered Technical Interview Platform</p>
            
        </div>
    """, unsafe_allow_html=True)

    if "candidate_data" not in st.session_state:
        st.session_state["candidate_data"] = None

    # Beautiful sidebar with gradient
    with st.sidebar:
        st.markdown("""
            <div style="
                background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
                padding: 1.5rem;
                border-radius: 1rem;
                margin-bottom: 1.5rem;
                border: 1px solid #3498db;
                box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            ">
                <h3 style="
                    color: #3498db; 
                    margin: 0 0 1rem 0; 
                    font-size: 1.2rem;
                    text-align: center;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 0.5rem;
                ">👤 Profile Preview</h3>
            </div>
        """, unsafe_allow_html=True)
        
        if st.session_state["candidate_data"]:
            cd = st.session_state["candidate_data"]
            # Individual info items with icons and better styling
            info_items = [
                ("👤", "Name", cd['full_name']),
                ("📧", "Email", cd['email']),
                ("📱", "Phone", cd['phone']),
                ("⏱️", "Experience", f"{cd['years_experience']} years"),
                ("💼", "Position", cd['desired_position']),
                ("📍", "Location", cd['current_location']),
                ("🛠️", "Tech Stack", cd['tech_stack'])
            ]
            
            for icon, label, value in info_items:
                st.markdown(f"""
                    <div style="
                        background: rgba(52, 73, 94, 0.6);
                        padding: 0.8rem;
                        border-radius: 0.8rem;
                        margin-bottom: 0.5rem;
                        border-left: 4px solid #3498db;
                    ">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-size: 1.2rem;">{icon}</span>
                            <div>
                                <div style="color: #bdc3c7; font-size: 0.8rem; margin-bottom: 0.2rem;">{label}</div>
                                <div style="color: #ecf0f1; font-weight: 500;">{value}</div>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="
                    background: rgba(52, 73, 94, 0.6);
                    padding: 1.5rem;
                    border-radius: 0.8rem;
                    text-align: center;
                    border: 2px dashed #3498db;
                ">
                    <div style="color: #bdc3c7; font-size: 0.9rem; margin-bottom: 0.5rem;">📋</div>
                    <div style="color: #ecf0f1; font-size: 0.9rem; font-weight: 500;">Fill the form to see your profile here</div>
                </div>
            """, unsafe_allow_html=True)

    if not st.session_state["candidate_data"]:
        # Simple form container
        st.markdown("""
            <div style="
                text-align: center;
                margin: 0 auto 2rem auto;
                max-width: 600px;
            ">
                <h2 style="
                    color: #3498db; 
                    margin: 0 0 1.5rem 0; 
                    font-size: 1.6rem;
                    font-weight: 600;
                ">🎯 Candidate Registration</h2>
                <div style="
                    background: rgba(52, 152, 219, 0.05);
                    padding: 1.5rem;
                    border-radius: 1rem;
                    border: 1px solid rgba(52, 152, 219, 0.2);
                ">
                    <p style="
                        color: #b0b8c1; 
                        font-size: 1rem; 
                        margin: 0;
                        font-weight: 400;
                    ">Please fill in your details below to get started with your technical interview</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        with st.form("candidate_form"):
            # Create two columns for better layout
            col1, col2 = st.columns(2)
            
            with col1:
                full_name = st.text_input(
                    "👤 Full Name", 
                    placeholder="e.g. John Doe",
                    help="Enter your full legal name"
                )
                
                email = st.text_input(
                    "📧 Email Address", 
                    placeholder="e.g. john.doe@email.com",
                    help="Enter your professional email address"
                )
                
                phone = st.text_input(
                    "📱 Phone Number", 
                    placeholder="e.g. +917034377828",
                    help="Enter your contact number with country code"
                )
                
                years_experience = st.number_input(
                    "⏱️ Years of Experience", 
                    min_value=0, 
                    max_value=60, 
                    step=1, 
                    placeholder="e.g. 5",
                    help="Select your total years of professional experience"
                )
            
            with col2:
                desired_position = st.text_input(
                    "💼 Desired Position(s)", 
                    placeholder="e.g. Software Engineer",
                    help="Enter the role you're applying for"
                )
                
                current_location = st.text_input(
                    "📍 Current Location", 
                    placeholder="e.g. India",
                    help="Enter your current city/country"
                )
                
                tech_stack = st.text_area(
                    "🛠️ Tech Stack (comma separated)", 
                    placeholder="e.g. Python, NLP, SQL, Machine Learning",
                    help="List your technical skills and technologies",
                    height=100
                )
            
            # Beautiful submit button
            # st.markdown("""
            #     <div style="text-align: center; margin: 2rem 0;">
            #         <div style="
            #             background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
            #             padding: 1rem 2rem;
            #             border-radius: 1rem;
            #             display: inline-block;
            #             box-shadow: 0 4px 20px rgba(0, 184, 148, 0.3);
            #         ">
            #             <p style="
            #                 color: white; 
            #                 font-size: 1.1rem; 
            #                 font-weight: 600; 
            #                 margin: 0;
            #             ">🚀 Ready to start your interview?</p>
            #         </div>
            #     </div>
            # """, unsafe_allow_html=True)
            
            submit = st.form_submit_button(
                "🎯 Start My Interview Journey", 
                type="primary", 
                use_container_width=True
            )

        if submit:
            candidate_data = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "years_experience": years_experience,
                "desired_position": desired_position,
                "current_location": current_location,
                "tech_stack": tech_stack,
            }
            is_valid, error = validate_candidate_data(candidate_data)
            if not is_valid:
                st.error(f"❌ Validation Error: {error}")
            else:
                with st.spinner("💾 Saving your information..."):
                    success = insert_candidate_data(candidate_data)
                if success:
                    st.session_state["candidate_data"] = candidate_data
                    st.session_state["start_interview"] = True
                    
                    # Success message
                    st.markdown("""
                        <div style="
                            background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
                            padding: 2rem;
                            border-radius: 1.5rem;
                            text-align: center;
                            margin: 2rem 0;
                            box-shadow: 0 8px 32px rgba(0, 184, 148, 0.3);
                        ">
                            <h2 style="
                                color: white; 
                                margin-bottom: 1rem;
                                font-size: 1.8rem;
                                text-shadow: 0 2px 4px rgba(0,0,0,0.3);
                            ">🎉 Registration Successful!</h2>
                            <p style="
                                color: rgba(255,255,255,0.9); 
                                margin-bottom: 1.5rem;
                                font-size: 1.1rem;
                            ">Your profile has been saved. Redirecting to your interview...</p>
                            <div style="
                                background: rgba(255,255,255,0.2);
                                padding: 1rem;
                                border-radius: 1rem;
                                display: inline-block;
                            ">
                                <p style="
                                    color: white; 
                                    font-size: 1rem; 
                                    font-weight: 600; 
                                    margin: 0;
                                ">⏳ Please wait...</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.rerun()
                else:
                    st.error("❌ Database Error: Could not save candidate information.")
    
    st.markdown('</div>', unsafe_allow_html=True)
