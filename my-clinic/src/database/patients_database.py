from src.connection.connection_db import ConnectionDB
from src.entities.patients import Patients

class PatientsDatabase:
    
    def findPatientAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Patients)
            result = db.session.query(Patients).all()
            return result