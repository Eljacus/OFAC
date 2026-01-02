from sqlalchemy import text
from db.connection import engine

def getPersonsToConsult():
    query = text("""
        SELECT
            p."idPersona",
            p."nombrePersona",
            p."aConsultar",
            m."direccion",
            m."pais"
        FROM "Personas" p
        INNER JOIN "MaestraDetallePersonas" m
            ON p."idPersona" = m."idPersona"
        WHERE p."aConsultar" LIKE '%Si%'
    """)

    with engine.connect() as conn:
        return conn.execute(query).fetchall()

def insertPersons(resultsPersons: list):
        queryInsert = text(
            """
            INSERT INTO "Resultadosuser7420"
            ("idPersona", "nombrePersona", "pais", "cantidadDeResultados", "estadoTransaccion")
            VALUES
            (:idPersona, :nombrePersona, :pais, :cantidadDeResultados, :estadoTransaccion)
        """)

        with engine.begin() as conn:
            conn.execute(queryInsert, resultsPersons)

def getPersonsNotMaster():
    query = text("""
        SELECT
            p."idPersona",
            p."nombrePersona",
            m."pais"
        FROM "Personas" p
        LEFT JOIN "MaestraDetallePersonas" m
            ON p."idPersona" = m."idPersona"
        WHERE m."idPersona" IS NULL
    """)
    with engine.begin() as conn:
       return conn.execute(query).fetchall()