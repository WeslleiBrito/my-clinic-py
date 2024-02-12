from src.database.type_exams_aso_database import TypeExamsAsoDatabase


class TypeExamsAsoBusiness(TypeExamsAsoDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findTypeExamsAsoAll(self):
        result = self.findTypeExamsAsoAll_db()
        
        datas = []
        for row in result:
            
            data = {
                "id": row.id,
                "name": row.name,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }
            
            datas.append(data)
        
        return datas
    

if __name__ == "__main__":
    class_type_exams_aso = TypeExamsAsoBusiness()
    datas = class_type_exams_aso.findTypeExamsAsoAll()
    print(datas)
    