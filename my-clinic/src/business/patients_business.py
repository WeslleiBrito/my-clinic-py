from src.database.patients_database import PatientsDatabase


class PatientsBusiness(PatientsDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findPatientsAll(self):
        result = self.findPatientAll_db()
        
        datas = []
        for row in result:
            
            data = {
                "id": row.id,
                "name": row.name,
                "rg": row.rg,
                "cpf": row.cpf,
                "createdAt": row.created_at,
                "updatedAt": row.updated_at
            }
            
            datas.append(data)
        
        return datas
    

if __name__ == "__main__":
    class_patient = PatientsBusiness()
    datas = class_patient.findPatientsAll()
    print(datas)
    