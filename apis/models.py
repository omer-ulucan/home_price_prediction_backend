from sqlalchemy import Column, Integer, Float
from database.db import Base

class Housing(Base):
    __tablename__ = "housing"
    
    id = Column(Integer, primary_key=True, index=True)
    total_rooms = Column(Integer, nullable=False)
    total_bedrooms = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    households = Column(Integer, nullable=False)
    median_income = Column(Integer, nullable=False)
    median_house_value = Column(Float) # Predicted price