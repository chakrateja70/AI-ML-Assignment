from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class CandidateInfo(Base):
    __tablename__ = "candidate_info"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    years_experience = Column(Integer, nullable=False)
    desired_position = Column(String(100), nullable=False)
    current_location = Column(String(100), nullable=False)
    tech_stack = Column(String(255), nullable=False)
