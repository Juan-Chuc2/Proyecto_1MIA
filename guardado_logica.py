import json
import os

ARCHIVO_CONFIG = "config.json"
ARCHIVO_TEMPORAL = "config.tmp"
ARCHIVO_RESPALDO = "config.bak"

Config_por_defecto = {
    "nombre_usuario": "usuario",
    "tema_interfaz": "claro",
    "idioma": "es",
    "tamaño_fuente": 13,
    "color_barra": "#1a1d28",
    "color_letra": "#000000",
    "foto_perfil": "",
}


def cargar_configuracion():

    if not os.path.exists(ARCHIVO_CONFIG):
        print("Aviso: no existe config.json, se usan valores por defecto.")
        return Config_por_defecto.copy()

    try:

        with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        config = Config_por_defecto.copy()
        config.update(datos)

        return config

    except json.JSONDecodeError:

        print("Aviso: config.json está corrupto, intentando restaurar desde config.bak")

        if os.path.exists(ARCHIVO_RESPALDO):

            try:

                with open(ARCHIVO_RESPALDO, "r", encoding="utf-8") as respaldo:
                    datos = json.load(respaldo)

                config = Config_por_defecto.copy()
                config.update(datos)

                return config

            except json.JSONDecodeError:

                print("Aviso: config.bak también está corrupto, se usan valores por defecto.")
                return Config_por_defecto.copy()

        else:

            print("Aviso: no hay config.bak, se usan valores por defecto.")
            return Config_por_defecto.copy()

    except PermissionError:

        print("Aviso: sin permisos de lectura sobre config.json, se usan valores por defecto.")
        return Config_por_defecto.copy()


def guardar_configuracion(datos):

    try:

        with open(ARCHIVO_TEMPORAL, "w", encoding="utf-8") as archivo:

            json.dump(
                datos,
                archivo,
                ensure_ascii=False,
                indent=4
            )

        if os.path.exists(ARCHIVO_CONFIG):

            try:

                with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as origen:
                    contenido_actual = origen.read()

                with open(ARCHIVO_RESPALDO, "w", encoding="utf-8") as respaldo:
                    respaldo.write(contenido_actual)

            except PermissionError:

                print("Aviso: no se pudo crear config.bak por falta de permisos.")

        os.replace(ARCHIVO_TEMPORAL, ARCHIVO_CONFIG)

        print("Configuración guardada correctamente en config.json")

        return True

    except PermissionError:

        print("Error: sin permisos de escritura, no se pudo guardar la configuración.")

        return False