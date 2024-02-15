from src.connection.connection_db import ConnectionDB
from src.entities.companies import Companies


class CompaniesDatabase:
    
    def _findCompanytAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).all()
            return result
    
    def _findCompanyById_db(self, id: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).filter_by(id = id).first()
            return result
        
    def _findCompanyByCNPJ_db(self, cnpj: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).filter_by(cnpj = cnpj).first()
            return result
        
    def _findCompanyByName_db(self, name: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("companies", Companies)
            result = db.session.query(Companies).filter_by(name = name).first()
            return result