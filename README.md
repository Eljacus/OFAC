# Validación de Personas contra OFAC

    **Autor:** Jacob Arévalo  
    **Lenguaje:** Python 3  
    **Base de datos:** PostgreSQL 


# Descripción general

    Este proyecto realiza la validación de personas en la plataforma **OFAC** consultadas desde Postgresql.


# Guia de instalacion del proyecto

# Clonar repositorio

    git clone https://github.com/Eljacus/OFAC
    cd OFAC

# Crear entorno virtual

    python -m venv .venv

# Instalar dependencias o librerias

    pip install -r requirements.txt

# Config. archivo .env (Cadena de conexion a db Postgresql)

    - Crear archivo .env dentro de la carpeta raiz (OFAC)
    - Crear la variable de entorno llamada:
    DATABASE_URL

    - Estructura:
    nombreVariable = "Cadena de conexion"

# Ejecucion de la prueba tecnica:

    Ejecutar desde el modulo main.py


