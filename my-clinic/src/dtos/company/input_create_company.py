from marshmallow import Schema, fields, ValidationError, validate
from pprint import pprint

class CreateCompanySchema(Schema):
    name = fields.String(
        required = True, error_messages = {"invalid": "Espera-se uma string."},
        validate = validate.Length(
            min = 3,
            error = "O nome precisa ter pelo menos 3 caracteres."
        )
    )
    cnpj = fields.String(required = True, validate = validate.Length(min = 14))


def validate_create_company_schema(name: str, cnpj: str):
    try:
        CreateCompanySchema().load({
            "name": name,
            "cnpj": cnpj
        })
        
        print("Validação feita com sucesso")
    except ValidationError as error:
        pprint(error.messages)

validate_create_company_schema(name="", cnpj="2364931")