from src.connection.base import Base
from src.entities.companies import Companies
from src.entities.patients import Patients
from src.entities.type_exams_aso import TypeExamsAso
from sqlalchemy import Column, String, DateTime, Integer, Numeric, ForeignKey
from datetime import datetime

class Forms(Base):
    
    __tablename__ = "forms"
    
    id = Column(String, primary_key = True)
    id_type_exam = Column(String, ForeignKey(TypeExamsAso.id))
    id_company = Column(String, ForeignKey(Companies.id))
    name_company = Column(String, nullable = False)
    id_patient = Column(String, ForeignKey(Patients.id))
    name_patient = Column(String, nullable = False)
    rg = Column(String, nullable = False, unique = True)
    cnpj = Column(String, nullable = False, unique = True)
    cpf = Column(String, unique = True)
    function_patient = Column(String, nullable = False)
    number_procedures = Column(Integer, nullable = False)
    status_exam = Column(Integer, nullable = False)
    amount = Column(Numeric(precision = 10, scale=2))
    comments = Column(String)
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    
    
    