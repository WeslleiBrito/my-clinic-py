from src.connection.connection_db import ConnectionDB
from src.entities.companies import Companies

class CompaniesDatabase:
    
    def findCompanytAll_db(self):
        with ConnectionDB() as db:
            result = db.session.query(Companies).all()
            return result