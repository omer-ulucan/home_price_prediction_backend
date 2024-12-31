from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    DATABASE_URL = "sqlite:///./database/db.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_threads": False})
    SessionLocal = sessionmaker(autocommit=False, 
                                autoflush=False, 
                                bind=engine)
    Base = declarative_base()
except Exception as e:
    raise Exception(f"Error setting up database connection with SQLAlchemy: {e}")
