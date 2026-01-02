def validatePerson(persona):
    if persona.direccion is None or persona.pais is None:
        return "Informacion incompleta"
    return "OK"


