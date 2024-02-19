import uuid
def validate_uuid(value):
    try:
        uuid_obj = uuid.UUID(value)
    except ValueError:
        raise ValidationError("Formato UUID inválido.")