from src.connection.base import Base
from sqlalchemy import Column, String, ForeignKey
from src.entities.forms import Forms
from src.entities.occupational_risks import OccupationalRisks

class OccupationalRisksForms(Base):
    
    __tablename__ = "occupational_risks_forms"
    
    id = Column(String(256), primary_key = True)
    name_risk = Column(String(256), nullable = False)
    id_form = Column(String(256), ForeignKey(Forms.id, onupdate='CASCADE', ondelete='CASCADE'))
    id_risk = Column(String(256), ForeignKey(OccupationalRisks.id, onupdate='CASCADE', ondelete='CASCADE'))
 
    
    