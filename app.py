"""
TalentScout - AI-Powered Hiring Assistant

This is the main entry point for the TalentScout application.
The application provides an intelligent chatbot for initial candidate
screening and technical assessment using AI-powered question generation
and response analysis.

Run this file with: streamlit run app.py
"""

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the main application
from app.main import main

if __name__ == "__main__":
    main()
