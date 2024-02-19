from src.database.companies_database import CompaniesDatabase
from src.dtos.company.input_create_company import CreateCompanySchema
from src.dtos.company.input_edit_company import EditCompanySchema
from src.erros.duplicity_error import DuplicityError
from src.erros.not_found_error import NotFoundError
from marshmallow import ValidationError
from datetime import datetime
import locale
import uuid

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

class CompaniesBusiness(CompaniesDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findCompanyAll(self, order : bool = False):
        result = self._findCompanytAll_db()
        
        datas = []
        for row in result:
            
            data = {
                "id": row.id,
                "name": row.name,
                "cnpj": row.cnpj,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }
            
            datas.append(data)
        
        return sorted(datas, key=lambda x: locale.strxfrm(x['name']), reverse = order)
    
    def findCompanyById(self, id: str):
        result = self._findCompanyById_db(id = id)
        return result
    
    def findCompanyByName(self, name: str, order : bool = False):
        result = self._findCompanyByName_db(name)
        datas = []
        for row in result:
            
            data = {
                "id": row.id,
                "name": row.name,
                "cnpj": row.cnpj,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }
            
            datas.append(data)
        
        return sorted(datas, key=lambda x: locale.strxfrm(x['name']), reverse = order)
    
    def create_company(self, name: str, cnpj: str):
        try:
            
            CreateCompanySchema().load({
                "name": name,
                "cnpj": cnpj
            })
            
            cnpj_exist = self._findCompanyByCNPJ_db(cnpj = "".join(filter(str.isdigit, cnpj)))
            
            if cnpj_exist:
                raise DuplicityError("O cnpj informado já exite em nossa base de dados.")
            
            name_exist = self._findCompanyByName_db(name = name.lower())
            
            if name_exist:
                raise DuplicityError("O nome informado já exite em nossa base de dados.")
            
            id = uuid.uuid4()
            
            self._create_company(
                id,
                name,
                "".join(filter(str.isdigit, cnpj))
            )
            
            print("Cadastro efeuado com sucesso!")
        except ValidationError as error:
         print(error.messages)
    def edit_company(self, id: str, name: str | None = None, cnpj: str | None = None):
        try:
                        
            id_exist = self.findCompanyById(id)
            
            if not id_exist:
                raise  NotFoundError("O id informado não existe")
            
            EditCompanySchema().load({
                "name": name  or id_exist.name,
                "cnpj": cnpj or id_exist.cnpj
            })
            
            if(name):
                
                name_exist = self._findCompanyByName_db(name=name.lower())
                
                if name_exist:
                    raise DuplicityError("O nome informado já exite em nossa base de dados.")
                
            if(cnpj):
                
                cnpj_exist = self._findCompanyByCNPJ_db(cnpj = "".join(filter(str.isdigit, cnpj)))

                if cnpj_exist:
                    raise DuplicityError("O cnpj informado já exite em nossa base de dados.")

            
            name = name or id_exist.name
            cnpj = cnpj or id_exist.cnpj
            newDate = datetime.now()
            
            self._edit_company(
                id ,
                name,
                "".join(filter(str.isdigit, cnpj)),
                    newDate
            )

            print("Edição efeuado com sucesso!")
        except ValidationError as error:
         print(error.messages)
    
    def delete_company(self, id: str):
        try:
            company_exist = self.findCompanyById(id)
            
            if not company_exist:
                raise  NotFoundError("O id informado não existe")
            
            self._delete_company(id)
            print("Registro deletado com sucesso!")
        except ValidationError as error:
         print(error.messages)
                
        

if __name__ == "__main__":
    class_business = CompaniesBusiness()
    class_business.edit_company("0002", "Papa")
    result = class_business.findCompanyAll() 
    
    for r in result:
        print(r)

   

    