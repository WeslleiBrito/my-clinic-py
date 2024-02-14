from src.connection.base import Base
from sqlalchemy import Column, String, ForeignKey, DateTime, Numeric
from src.entities.forms import Forms
from src.entities.exams import Exams
from datetime import datetime

class ProceduresForms(Base):
    
    __tablename__ = "procedures_forms"
    
    id = Column(String(256), primary_key = True)
    id_form = Column(String(256), ForeignKey(Forms.id, onupdate='CASCADE', ondelete='CASCADE'), nullable = False)
    id_exam = Column(String(256), ForeignKey(Exams.id, onupdate='CASCADE', ondelete='CASCADE'), nullable = False)
    name_exam = Column(String(256), nullable = False)
    date = Column(DateTime, nullable = False)
    price = Column(Numeric(precision = 10, scale=2), default = 0)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
 
    
    