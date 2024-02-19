from src.connection.connection_db import ConnectionDB
from src.entities.patients import Patients

class PatientsDatabase:

    def _findPatientsAll_db(self):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("patients", Patients)
            result = db.session.query(Patients).all()
            return result

    def _findPatientById_db(self, id: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("patients", Patients)
            result = db.session.query(Patients).filter_by(id=id).first()
            return result

    def _findPatientByCPF_db(self, cpf: str):
        with ConnectionDB() as db:
            db.create_table_if_not_exists("patients", Patients)
            result = db.session.query(Patients).filter_by(cpf=cpf).first()
            return result

    def _findCompanyByName_db(self, name: str):

        with ConnectionDB() as db:
            db.create_table_if_not_exists("patients", Patients)
            result = db.session.query(Patients).filter(func.lower(Patients.name).ilike(f'%{name.lower()}%')).all()
            return result

    def _create_patient(self, id: str, name: str, rg: str,cpf: str):
        with ConnectionDB() as db:
            newDatas = Patients(id, name, rg, cpf)

            try:
                db.create_table_if_not_exists("patients", Patients)
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