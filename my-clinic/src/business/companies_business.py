from src.database.companies_database import CompaniesDatabase
from src.dtos.company.input_create_company import CreateCompanySchema
from marshmallow import ValidationError

class CompaniesBusiness(CompaniesDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findCompanyAll(self):
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
        
        return datas
    
    def findCompanyById(self, id: str):
        result = self._findCompanyById_db(id = id)
        return result
        
    def create_company(self, name: str, cnpj: str):
        try:
            
            CreateCompanySchema().load({
                "name": name,
                "cnpj": cnpj
            })
            
            
            print("Cadastro efeuado com sucesso!")
        except ValidationError as error:
         print(error.messages)
            
if __name__ == "__main__":
    class_business = CompaniesBusiness()
    class_business.create_company(name = "Nova Burite", cnpj="29.369.431/0001-01")
    class_business.findCompanyAll()
    class_business.findCompanyById(id="125446ss6s4vf")
   

    