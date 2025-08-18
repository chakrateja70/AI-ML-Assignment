import re
from typing import Dict, Any, Tuple
from app.db.mysql import get_db_connection

def validate_candidate_data(data: Dict[str, Any]) -> Tuple[bool, str]:
	"""
	Validate candidate details.
	Returns (is_valid, error_message)
	"""
	if not data.get("full_name"):
		return False, "Full name is required."
	if not data.get("email") or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", data["email"]):
		return False, "Invalid email address."
	if not data.get("phone") or not re.match(r"^(\+91[ -]?|91[ -]?|0)?\d{10}$", data["phone"]):
		return False, "Invalid phone number. Allowed formats: +91 7032377949, +917032377949, 7032377949."

	try:
		years = int(data.get("years_experience", 0))
		if years < 0:
			return False, "Years of experience must be a positive integer."
	except ValueError:
		return False, "Years of experience must be a number."
	if not data.get("desired_position"):
		return False, "Desired position is required."
	if not data.get("current_location"):
		return False, "Current location is required."
	if not data.get("tech_stack"):
		return False, "Tech stack is required."
	return True, ""

def insert_candidate_data(data: Dict[str, Any]) -> bool:
	"""
	Insert candidate data into the database.
	Returns True if successful, False otherwise.
	"""
	try:
		conn = get_db_connection()
		cursor = conn.cursor()
		query = (
			"INSERT IGNORE INTO candidate_info (full_name, email, phone, years_experience, desired_position, current_location, tech_stack)"
			"VALUES (%s, %s, %s, %s, %s, %s, %s)"
		)
		values = (
			data["full_name"],
			data["email"],
			data["phone"],
			data["years_experience"],
			data["desired_position"],
			data["current_location"],
			data["tech_stack"],
		)
		cursor.execute(query, values)
		conn.commit()
		cursor.close()
		conn.close()
		return True
	except Exception as e:
		print(f"Error inserting candidate data: {e}")
		return False
