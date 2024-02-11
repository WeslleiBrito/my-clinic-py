from src.database.companies_database import CompaniesDatabase


class CompaniesBusiness(CompaniesDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findCompanytAll(self):
        result = self.findCompanytAll_db()
        
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
    

if __name__ == "__main__":
    class_business = CompaniesBusiness()
    datas = class_business.findCompanytAll()
    print(datas)
    