SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public' 

SELECT * FROM "Resultadosuser7420" WHERE "estadoTransaccion" LIKE '%Información incompleta%'
SELECT * FROM "MaestraDetallePersonas" WHERE "idPersona" IS NULL
SELECT * FROM "Personas"

DELETE FROM "Resultadosuser7420"

        SELECT
            p."idPersona",
            p."nombrePersona",
            p."aConsultar",
            m."direccion",
            m."pais"
        FROM "Personas" p
        LEFT JOIN "MaestraDetallePersonas" m
            ON p."idPersona" = m."idPersona"
        WHERE p."aConsultar" LIKE '%Si%'
		AND m."direccion" IS NOT NULL 
			AND m."pais" IS NOT NULL

		SELECT
		COUNT(*)
        FROM "Personas" p
        LEFT JOIN "MaestraDetallePersonas" m
            ON p."idPersona" = m."idPersona"
        WHERE p."aConsultar" LIKE '%Si%'
		AND (m."direccion" IS NOT NULL 
			AND m."pais" IS NOT NULL)


			UPDATE "MaestraDetallePersonas" SET "Pais" = 'Colombia' WHERE "id" = '44'


			SELECT
    p."idPersona" AS "PERSONAS",
	m."idPersona" AS "MASTER",
    p."nombrePersona",
    p."aConsultar",
    m."direccion",
    m."pais"
FROM "Personas" p
LEFT JOIN "MaestraDetallePersonas" m
    ON p."idPersona" = m."idPersona"
WHERE m."idPersona" IS NULL