from src.database.procedures_forms_database import ProceduresFormsDatabase


class ProceduresFormsBusiness(ProceduresFormsDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findProceduresFormsAll(self):
        result = self.findProceduresFormsAll_db()
        
        datas = []
        for row in result:
            
            data = {
                "id": row.id,
                "nameExam": row.name_exam,
                "idExam": row.id_exam,
                "idForm": row.id_form,
                "date": row.date,
                "price": row.price,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }
            
            datas.append(data)
        
        return datas
    

if __name__ == "__main__":
    class_procedures_forms_risks = ProceduresFormsBusiness()
    datas = class_procedures_forms_risks.findProceduresFormsAll()
    print(datas)
    