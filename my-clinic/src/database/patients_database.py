from src.connection.connection_db import ConnectionDB
from src.entities.patients import Patients

class PatientsDatabase:
    
    def findPatientAll_db(self):
        with ConnectionDB() as db:
            result = db.session.query(Patients).all()
            return result