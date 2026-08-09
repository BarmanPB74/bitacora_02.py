GNU nano 9.1       bitacora_04.py
#!/usr/bin/env python3

import json
import os


ARCHIVO_BITACORA = "bitacora.json"


# ===== Funciones =====

def cargar_bitacora(nombre_archivo=ARCHIVO_BITACORA):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf>
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                print("El archivo está vacío o dañad>
                return []

    return []


def saludar():
    print("Hola jefe")


def crear_reporte():
    reporte = {
        "titulo": input("Título: "),
        "fecha": input("Fecha: "),
        "hora": input("Hora: "),
        "proyecto": input("Proyecto: "),
        "tipo": input("Tipo: "),
        "contenido": input("Contenido: ")
    }

    return reporte


def guardar_bitacora(bitacora, nombre_archivo=ARCHIV>
    with open(nombre_archivo, "w", encoding="utf-8")>
        json.dump(
            bitacora,
            archivo,
            indent=4,
            ensure_ascii=False
        )


# ===== Programa principal =====


if __name__ == "__main__":
    saludar()

    bitacora = cargar_bitacora()

    nuevo = crear_reporte()
    bitacora.append(nuevo)

    guardar_bitacora(bitacora)

    print(f"\nReporte guardado. Total de reportes: {len(bitacora)}")
