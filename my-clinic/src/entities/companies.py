from src.connection.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

class Companies(Base):
    __tablename__ = "companies"
    
    id = Column(String, primary_key = True)
    name = Column(String, nullable = False)
    cnpj = Column(String, nullable = False, unique = True)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    
    