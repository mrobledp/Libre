
import json
from pathlib import Path
from collections import defaultdict

# Diccionario global para almacenar valores únicos por campo simple
valores_campos = defaultdict(set)

def recolectar_valores(clave, valor):
    """Registra valores simples en el diccionario global."""
    if isinstance(valor, (str, int, float, bool)) or valor is None:
        if len(valores_campos[clave]) < 30:
            valores_campos[clave].add(valor)

def analizar_bloques(data, nivel=0, prefijo=""):
    """
    Recorre el JSON y detecta bloques principales:
    - Objetos (dict)
    - Listas (list)
    - Tamaño de listas
    Además, recolecta valores simples.
    """
    indent = "  " * nivel

    if isinstance(data, dict):
        for clave, valor in data.items():
            nombre_campo = f"{prefijo}.{clave}" if prefijo else clave

            if isinstance(valor, dict):
                print(f"{indent}- Objeto: {clave}")
                analizar_bloques(valor, nivel + 1, nombre_campo)

            elif isinstance(valor, list):
                print(f"{indent}- Lista: {clave} (elementos: {len(valor)})")

                # Analizar TODOS los elementos, no solo el primero
                for elemento in valor:
                    analizar_bloques(elemento, nivel + 1, nombre_campo)

            else:
                print(f"{indent}- Campo: {clave} (valor simple)")
                recolectar_valores(nombre_campo, valor)

    elif isinstance(data, list):
        print(f"{indent}- Lista anónima (elementos: {len(data)})")
        for elemento in data:
            analizar_bloques(elemento, nivel + 1, prefijo)


def generar_reporte(ruta_archivo):
    ruta = Path(ruta_archivo)

    if not ruta.exists():
        print(f"ERROR: No se encontró el archivo {ruta}")
        return

    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("\n=== REPORTE DE BLOQUES PRINCIPALES ===\n")
    analizar_bloques(data)
    print("\n=== FIN DEL REPORTE DE BLOQUES ===\n")

    print("\n=== VALORES DISTINTOS POR CAMPO SIMPLE (máx 30) ===\n")
    for campo, valores in valores_campos.items():
        print(f"- {campo}:")
        i=0
        for v in valores:
            i += 1
            print(f"    {i:02d}\u27A1 {v}")
        print()

    print("=== FIN DEL REPORTE ===\n")

if __name__ == "__main__":
    archivo_json = input("Nombre del archivo JSON a analizar (ej. catalogo_complejo.json): ")
    if archivo_json.endswith(".json"):pass
    else: archivo_json += ".json"
    generar_reporte(archivo_json)