import streamlit as st

from app.ui.candidate_form import candidate_form
from app.ui.chatbot_ui import chatbot_ui

def main():
	if "candidate_data" not in st.session_state or not st.session_state["candidate_data"]:
		candidate_form()
	elif st.session_state.get("start_interview", False):
		chatbot_ui()
	else:
		candidate_form()