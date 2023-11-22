import random as rdm
import csv

nombre_archivo = "alumnos.csv"
cantidad_alumnos = []
alumnos_leidos = []
try:
    with open(nombre_archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            alumnos_leidos.append(row)
        while alumnos_leidos != "":
            row = rdm.choice(alumnos_leidos)
            print(row)
            alumnos_leidos.remove(row)
except Exception as ex:
    print(ex)