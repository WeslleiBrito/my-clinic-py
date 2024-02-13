from src.connection.connection_db import ConnectionDB
from src.entities.type_exams_aso import TypeExamsAso

class TypeExamsAsoDatabase:
    
    def findTypeExamsAsoAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", TypeExamsAso)
            result = db.session.query(TypeExamsAso).all()
            return result