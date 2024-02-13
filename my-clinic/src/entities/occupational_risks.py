from src.connection.base import Base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

class OccupationalRisks(Base):
    
    __tablename__ = "occupational_risks"
    
    id = Column(String(256), primary_key = True)
    name = Column(String(256), nullable = False)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    
    