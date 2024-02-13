from src.connection.connection_db import ConnectionDB
from src.entities.occupational_risks import OccupationalRisks

class OccupationalRisksDatabase:
    
    def findOccupationalRisksAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", OccupationalRisks)
            result = db.session.query(OccupationalRisks).all()
            return result