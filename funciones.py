#!/usr/bin/env python3

import json
import datetime

if __name__ == '__main__':


# ===== Funciones =====
def cargar_bitacora(nombre_archivo="bitcora.json")
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)
            except json.JSONDecodeError:
                print("El archivo está dañado, empezando nuevo reporte")
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


def guardar_bitacora(bitacora):
    with open("bitacora.json", "w") as archivo:
      json.dump(bitacora, archivo)


# ===== Programa principal =====

saludar()

bitacora = []

nuevo = crear_reporte()
bitacora.append(nuevo)
guardar_bitacora(bitacora)
print(nuevo)

