from marshmallow import Schema, fields, ValidationError, validate
from src.services.validate_rg import validate_rg
from src.services.validate_cnpj_cpf import ValidateCPFCNPJ

class CreatePatientSchema(Schema):
    
    name = fields.String(
        required=True,
        error_messages={"invalid": "Espera-se uma string."},
        validate=validate.Length(
            min=3,
            error="O nome precisa ter pelo menos 3 caracteres."
        )
    )
    
    rg = fields.String(
        required=True,
        error_messages={"invalid": "Espera-se uma string."},
        validate=[validate_rg]
    )
    
    cpf = fields.String(
        required=False,
        error_messages={"invalid": "Espera-se uma string."},
            validate=[ValidateCPFCNPJ().validate]
    )


def validate_create_patient_schema(name: str, rg: str, cpf: str = ""):
    try:
        CreatePatientSchema().load({
            "name": name,
            "rg": rg,
            "cpf": cpf
        })

        print("Validação feita com sucesso")
    except ValidationError as error:
        pprint(error.messages)

validate_create_patient_schema("Maria de Almeida", "13638538-99", "05353970543")