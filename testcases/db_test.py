import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.db.mysql import get_db_connection

def test_select_all_candidates():
	conn = get_db_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM candidate_info")
	results = cursor.fetchall()
	for row in results:
		print(row)
	cursor.close()
	conn.close()

if __name__ == "__main__":
	test_select_all_candidates()
