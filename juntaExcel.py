import os
import pandas as pd

# Carpeta donde están los Excel
CARPETA_EXCEL = "./"
SALIDA_CSV = "salida.csv"

def procesar_excels(carpeta, salida_csv):
    filas_salida = []

    # Extensiones válidas
    extensiones = (".xlsx", ".xls", ".xlsm")

    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith(extensiones):
            ruta = os.path.join(carpeta, archivo)
            print(f"Procesando: {archivo}")

            # Cargar todas las hojas
            xls = pd.ExcelFile(ruta)

            for hoja in xls.sheet_names:
                df = pd.read_excel(ruta, sheet_name=hoja, dtype=str)  # dtype=str para no perder formatos

                # Rellenar NaN con cadena vacía
                df = df.fillna("")

                for _, fila in df.iterrows():
                    filas_salida.append(
                        [archivo, hoja] + fila.tolist()
                    )

    # Guardar CSV sin cabecera
    pd.DataFrame(filas_salida).to_csv(salida_csv, index=False, header=False, encoding="utf-8")

    print(f"CSV generado: {salida_csv}")


if __name__ == "__main__":
    procesar_excels(CARPETA_EXCEL, SALIDA_CSV)