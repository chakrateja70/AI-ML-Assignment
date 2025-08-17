import streamlit as st
from .utils.helpers import validate_candidate_data
from app.utils.helpers import insert_candidate_data


def main():
	st.title("TalentScout - Candidate Registration")
	st.write("Please enter your details below:")

	with st.form("candidate_form"):
		full_name = st.text_input("Full Name")
		email = st.text_input("Email Address")
		phone = st.text_input("Phone Number")
		years_experience = st.number_input("Years of Experience", min_value=0, max_value=60, step=1)
		desired_position = st.text_input("Desired Position(s)")
		current_location = st.text_input("Current Location")
		tech_stack = st.text_area("Tech Stack (comma separated)")
		submit = st.form_submit_button("Submit")

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
			st.error(f"Validation Error: {error}")
		else:
			if insert_candidate_data(candidate_data):
				st.success("Candidate information saved successfully!")
			else:
				st.error("Database Error: Could not save candidate information.")
