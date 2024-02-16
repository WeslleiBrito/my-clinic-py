from src.database.companies_database import CompaniesDatabase
from src.dtos.company.input_create_company import CreateCompanySchema
from src.erros.duplicity_error import DuplicityError
from marshmallow import ValidationError
import locale

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
            
            id = "0003"
            
            self._create_company(
                id,
                name,
                "".join(filter(str.isdigit, cnpj))
            )
            
            print("Cadastro efeuado com sucesso!")
        except ValidationError as error:
         print(error.messages)
            
if __name__ == "__main__":
    class_business = CompaniesBusiness()
    result = class_business.findCompanyAll(order = True) 
    
    for r in result:
        print(r)

   

    