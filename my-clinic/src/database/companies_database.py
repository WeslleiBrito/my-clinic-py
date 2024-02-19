from src.connection.connection_db import ConnectionDB
from src.entities.companies import Companies
from sqlalchemy.exc import IntegrityError
from src.dtos.operation_not_completed_error import OperationNotCompletedError
from sqlalchemy import func
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
            result = db.session.query(Companies).filter(func.lower(Companies.name).ilike(f'%{name.lower()}%')).all()
            return result
        
    def _create_company(self, id: str, name: str, cnpj: str):
        with ConnectionDB() as db:
            newDatas = Companies(id, name, cnpj)
            
            try:
                db.create_table_if_not_exists("companies", Companies)
                db.session.add(newDatas)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                raise OperationNotCompletedError("Tivemos um problema ao inserir os novos dados: ") from e 
    
    def _edit_company(self, id: str, name: str, cnpj: str):
        with ConnectionDB() as db:
            new_datas = Companies(id, name, cnpj)
            
            try:
                db.create_table_if_not_exists("companies", Companies)
                
                company = db.session.query(Companies).filter_by(id=id).first()
                company.name = name
                company.cnpj = cnpj
                db.session.commit()
                    
            except IntegrityError as e:
                db.session.rollback()
                raise OperationNotCompletedError("Tivemos um problema ao editar os dados: ") from e 
                
    def _delete_company(self, id: str):
        with ConnectionDB() as db:
            try:   
                company = db.session.query(Companies).filter_by(id=id).first()
                db.session.delete(company)
                db.session.commit()
            except IntegrityError as e:
                db.session.rollback()
                raise OperationNotCompletedError("Tivemos um problema ao deletar os dados: ") from e 