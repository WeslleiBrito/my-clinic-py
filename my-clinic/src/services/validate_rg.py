import re
def validate_rg(value: str):

    if not re.match(r'^(\d{2}\.?\d{3}\.?\d{3}-?\d{2})|(\d{10})$', value):
        raise ValueError("Rg inválido!")