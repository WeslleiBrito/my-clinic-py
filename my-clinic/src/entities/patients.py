from src.connection.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

class Patients(Base):
    
    __tablename__ = "patients"
    
    id = Column(String, primary_key = True)
    name = Column(String, nullable = False)
    rg = Column(String, nullable = False, unique = True)
    cpf = Column(String, unique = True)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    
    