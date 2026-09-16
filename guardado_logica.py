import json
import os
import re

ARCHIVO_CONFIG = "config.json"
ARCHIVO_TEMPORAL = "config.tmp"
ARCHIVO_RESPALDO = "config.bak"

IDIOMAS_VALIDOS = {"es", "es-ES", "en", "en-US"}
TEMAS_VALIDOS = {"claro", "oscuro"}
PATRON_COLOR = re.compile(r"^#(?:[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")

Config_por_defecto = {
    "nombre_usuario": "usuario",
    "tema_interfaz": "claro",
    "idioma": "es",
    "tamaño_fuente": 13,
    "color_barra": "#1a1d28",
    "color_letra": "#000000",
    "foto_perfil": "",
}


def validar_configuracion(datos):

    if not isinstance(datos, dict):
        return False, "el contenido no es un objeto de configuración (no es un diccionario JSON)."

    claves_esperadas = set(Config_por_defecto.keys())
    if not claves_esperadas.issubset(datos.keys()):
        faltantes = claves_esperadas - datos.keys()
        return False, f"faltan campos obligatorios: {', '.join(sorted(faltantes))}."

    if not isinstance(datos["nombre_usuario"], str) or not datos["nombre_usuario"].strip():
        return False, "'nombre_usuario' debe ser un texto no vacío."

    if datos["tema_interfaz"] not in TEMAS_VALIDOS:
        return False, "'tema_interfaz' debe ser 'claro' u 'oscuro'."

    if datos["idioma"] not in IDIOMAS_VALIDOS:
        return False, f"'idioma' debe ser uno de: {', '.join(sorted(IDIOMAS_VALIDOS))}."

    if not isinstance(datos["tamaño_fuente"], int) or isinstance(datos["tamaño_fuente"], bool):
        return False, "'tamaño_fuente' debe ser un número entero."
    if not (6 <= datos["tamaño_fuente"] <= 72):
        return False, "'tamaño_fuente' debe estar entre 6 y 72."

    if not isinstance(datos["color_barra"], str) or not PATRON_COLOR.match(datos["color_barra"]):
        return False, "'color_barra' debe ser un color hexadecimal válido (ej. #1a1d28 o #ff1a1d28)."

    if not isinstance(datos["color_letra"], str) or not PATRON_COLOR.match(datos["color_letra"]):
        return False, "'color_letra' debe ser un color hexadecimal válido (ej. #000000 o #ff000000)."

    if not isinstance(datos["foto_perfil"], str):
        return False, "'foto_perfil' debe ser una ruta de texto (puede estar vacía)."

    return True, ""


def _restaurar_desde_respaldo(ruta_respaldo, motivo):

    print(f"Aviso: {motivo} Intentando restaurar desde config.bak")

    if not os.path.exists(ruta_respaldo):
        mensaje = f"{motivo} No existe config.bak para restaurar. Se usan valores por defecto."
        print(mensaje)
        return Config_por_defecto.copy(), mensaje, "formato_invalido"

    try:
        with open(ruta_respaldo, "r", encoding="utf-8") as respaldo:
            datos_respaldo = json.load(respaldo)
    except json.JSONDecodeError:
        mensaje = f"{motivo} El respaldo config.bak también está corrupto. Se usan valores por defecto."
        print(mensaje)
        return Config_por_defecto.copy(), mensaje, "corrupto"

    es_valido, detalle = validar_configuracion(datos_respaldo)
    if not es_valido:
        mensaje = f"{motivo} El respaldo config.bak tampoco es válido ({detalle}). Se usan valores por defecto."
        print(mensaje)
        return Config_por_defecto.copy(), mensaje, "formato_invalido"

    config = Config_por_defecto.copy()
    config.update(datos_respaldo)
    mensaje = f"{motivo} Se restauró la configuración desde config.bak."
    print(mensaje)
    return config, mensaje, "restaurado"


def cargar_configuracion(ruta=None):

    ruta_config = ruta if ruta else ARCHIVO_CONFIG
    carpeta = os.path.dirname(ruta_config) or "."
    ruta_respaldo = os.path.join(carpeta, "config.bak")

    if not os.path.exists(ruta_config):
        mensaje = "Aviso: el archivo no existe, se usan valores por defecto."
        print(mensaje)
        return Config_por_defecto.copy(), mensaje, "no_existe"

    try:
        with open(ruta_config, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except json.JSONDecodeError:
        return _restaurar_desde_respaldo(
            ruta_respaldo,
            "El archivo seleccionado tiene un JSON mal formado (sintaxis inválida)."
        )

    except PermissionError:
        mensaje = "Aviso: sin permisos de lectura sobre el archivo, se usan valores por defecto."
        print(mensaje)
        return Config_por_defecto.copy(), mensaje, "sin_permisos"

    es_valido, detalle = validar_configuracion(datos)
    if not es_valido:
        return _restaurar_desde_respaldo(
            ruta_respaldo,
            f"El archivo seleccionado no es una configuración válida de esta aplicación: {detalle}"
        )

    config = Config_por_defecto.copy()
    config.update(datos)
    mensaje = "Configuración cargada correctamente."
    return config, mensaje, "ok"


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

        mensaje = "Configuración guardada correctamente en config.json"
        print(mensaje)

        return True, mensaje

    except PermissionError:

        mensaje = "Error: sin permisos de escritura, no se pudo guardar la configuración."
        print(mensaje)

        return False, mensaje