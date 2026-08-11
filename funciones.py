#!/usr/bin/env python3

import json
import os


ARCHIVO_BITACORA = "bitacora.json"

CAMPOS_OBLIGATORIOS = (
    "titulo",
    "fecha",
    "hora",
    "proyecto",
    "tipo",
    "contenido"
)


# ===== Validaciones =====

def validar_reporte(reporte):
    if not isinstance(reporte, dict):
        return False

    for campo in CAMPOS_OBLIGATORIOS:
        if campo not in reporte:
            return False

        valor = reporte[campo]

        if not isinstance(valor, str):
            return False

        if not valor.strip():
            return False

    return True


def validar_bitacora(datos):
    if not isinstance(datos, list):
        return False

    for reporte in datos:
        if not validar_reporte(reporte):
            return False

    return True


# ===== Manejo de archivos =====

def cargar_bitacora(nombre_archivo=ARCHIVO_BITACORA):
    if not os.path.exists(nombre_archivo):
        return []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)

        except json.JSONDecodeError:
            print("El archivo está vacío o contiene JSON dañado.")
            return None

    if not validar_bitacora(datos):
        print("El JSON existe, pero su contenido no es válido.")
        return None

    return datos


def guardar_bitacora(bitacora, nombre_archivo=ARCHIVO_BITACORA):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(
            bitacora,
            archivo,
            indent=4,
            ensure_ascii=False
        )


# ===== Interacción =====

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


# ===== Programa principal =====

if __name__ == "__main__":
    saludar()

    bitacora = cargar_bitacora()

    if bitacora is None:
        print("Programa detenido para proteger los datos.")

    else:
        nuevo = crear_reporte()

        if not validar_reporte(nuevo):
            print("El nuevo reporte contiene campos vacíos o inválidos.")

        else:
            bitacora.append(nuevo)
            guardar_bitacora(bitacora)

            total_reportes = len(bitacora)

            print(
                f"\nReporte guardado. "
                f"Total de reportes: {total_reportes}"
            )