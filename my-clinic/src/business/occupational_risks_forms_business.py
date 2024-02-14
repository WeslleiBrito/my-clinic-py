from src.database.occupational_risks_forms_database import OccupationalRisksFormsDatabase


class OccupationalRisksFormsBusiness(OccupationalRisksFormsDatabase):
    
    def __init__(self):
        super().__init__()
    
    def findOccupationalRisksFormsAll(self):
        result = self.findOccupationalRisksFormsAll_db()
        
        datas = []
        for row in result:
            
            data = {
                "id": row.id,
                "nameRisk": row.name_risk,
                "idRisk": row.id_risk,
                "idForm": row.id_form
            }
            
            datas.append(data)
        
        return datas
    

if __name__ == "__main__":
    class_occupational_forms_risks = OccupationalRisksFormsBusiness()
    datas = class_occupational_forms_risks.findOccupationalRisksFormsAll()
    print(datas)
    