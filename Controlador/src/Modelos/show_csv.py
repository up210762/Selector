import csv

def mostrar_contenido_csv(archivo_csv):
    filas = []
    with open(archivo_csv, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)

        # Lee el contenido
        for fila in lector_csv:
            filas.append(fila)
        return fila