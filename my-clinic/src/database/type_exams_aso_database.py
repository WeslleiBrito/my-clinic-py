from src.connection.connection_db import ConnectionDB
from src.entities.type_exams_aso import TypeExamsAso

class TypeExamsAsoDatabase:
    
    def findTypeExamsAsoAll_db(self):
        with ConnectionDB() as db:
            result = db.session.query(TypeExamsAso).all()
            return result