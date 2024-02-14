from src.connection.connection_db import ConnectionDB
from src.entities.occupational_risks_forms import OccupationalRisksForms

class OccupationalRisksFormsDatabase:
    
    def findOccupationalRisksFormsAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("occupational_risks_forms", OccupationalRisksForms)
            result = db.session.query(OccupationalRisksForms).all()
            return result