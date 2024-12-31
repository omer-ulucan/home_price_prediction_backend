from sqlalchemy.orm import Session
from apis.models import Housing

def add_data_to_db(db: Session, housing_data: dict):
    new_entry = Housing(**housing_data)
    db.add(new_entry)
    db.commit()