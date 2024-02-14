from src.connection.connection_db import ConnectionDB
from src.entities.procedures_forms import ProceduresForms

class ProceduresFormsDatabase:
    
    def findProceduresFormsAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("procedures_forms", ProceduresForms)
            result = db.session.query(ProceduresForms).all()
            return result