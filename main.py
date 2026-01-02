from db.consults import getPersonsToConsult, insertPersons, getPersonsNotMaster
from services.validator import validatePerson
from utils.ManagementScreen import ManagementScreen
from utils.ManagementExcel import exportIncomplete

def main():
    navOfac = ManagementScreen()
    navOfac.openBrowser()
    persons = getPersonsToConsult()
    results = []
    personsNotMaster = getPersonsNotMaster()

    for p in personsNotMaster:
        results.append({
            "idPersona": p.idPersona,
            "nombrePersona": p.nombrePersona,
            "pais": p.pais,
            "cantidadDeResultados": 0,
            "estadoTransaccion": "No cruza con maestra"
        })


    for p in persons:
        statePerson = validatePerson(p)
        if statePerson != "OK":
            results.append(
                {
                    "idPersona": p.idPersona,
                    "nombrePersona": p.nombrePersona,
                    "pais": p.pais,
                    "cantidadDeResultados": 0,
                    "estadoTransaccion": validatePerson(p)
                }
            )
            continue
        try:
            amountResults = navOfac.searchPerson(p.nombrePersona, p.direccion, p.pais)
            if amountResults > 0:
                navOfac.MakeScreenshot(p.idPersona)

            results.append({
                "idPersona": p.idPersona,
                "nombrePersona": p.nombrePersona,
                "pais": p.pais,
                "cantidadDeResultados": amountResults,
                "estadoTransaccion": "OK"
            })
        except Exception as e:
            results.append({
                "idPersona": p.idPersona,
                "nombrePersona": p.nombrePersona,
                "pais": p.pais,
                "cantidadDeResultados": 0,
                "estadoTransaccion": "NOK"
            })
        
    #INSERCION MASIVA DE RESULTADOS
    navOfac.close()
    insertPersons(results)
    exportIncomplete(results)

if __name__ == "__main__":
    main()