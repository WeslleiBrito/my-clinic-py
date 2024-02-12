from src.connection.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

class TypeExamsAso(Base):
    
    __tablename__ = "type_exams_aso"
    
    id = Column(String, primary_key = True)
    name = Column(String, nullable = False)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    
    