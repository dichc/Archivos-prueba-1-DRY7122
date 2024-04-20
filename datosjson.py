import json
from datetime import datetime, timedelta

# Ruta del archivo JSON en la máquina virtual
ruta_archivo = "/home/devasc/labs/devnet-src/parsing/myfile.json"

try:
    # Abrir y cargar el archivo JSON en la variable ourjson utilizando json.load
    with open(ruta_archivo, "r") as archivo:
        ourjson = json.load(archivo)
        print("Archivo JSON cargado correctamente en 'ourjson'.")

    # Comprobar si el archivo contiene la información de los tokens
    if "access_token" in ourjson and "refresh_token" in ourjson:
        # Imprimir el valor del token
        access_token = ourjson["access_token"]
        refresh_token = ourjson["refresh_token"]
        print("Valor del access token:", access_token)
        print("Valor del refresh token:", refresh_token)

        # Calcular la fecha de caducidad del token de actualización
        expires_in = ourjson.get("expires_in", 0)
        refreshtokenexpires_in = ourjson.get("refreshtokenexpires_in", 0)
        fecha_caducidad_access_token = datetime.now() + timedelta(seconds=expires_in)
        fecha_caducidad_refresh_token = datetime.now() + timedelta(seconds=refreshtokenexpires_in)
        print("Fecha de caducidad del access token:", fecha_caducidad_access_token)
        print("Fecha de caducidad del refresh token:", fecha_caducidad_refresh_token)
    else:
        print("El archivo JSON no contiene la información necesaria para los tokens.")
except FileNotFoundError:
    print("El archivo JSON no se encontró en la ruta especificada.")
except Exception as e:
    print("Ocurrió un error al cargar el archivo JSON:", e)

