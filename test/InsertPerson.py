from db.consults import insertPersons
dummy = [
    {
        "idpersona": 999,
        "nombrepersona": "PRUEBA BOT",
        "pais": "CO",
        "cantidadderesultados": 5,
        "estadotransaccion": "OK"
    }
]

insertPersons(dummy)