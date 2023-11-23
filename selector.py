import random as rdm
import csv, os

nombre_archivo = input("Escribe el nombre del archivo con los alumnos a sortear: ")
nombre_archivo_nuevo = input("Escribe el nombre del archivo nuevo: ")
grupos_creados = int(input("¿Cuántos gupos se van a crear?: "))
alumnos_por_grupo = int(input("Número de alumnos por grupo: "))
alumnos_leidos = []

try:
    with open(nombre_archivo, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            alumnos_leidos.append(row)
    os.system(f"touch {nombre_archivo_nuevo}")
    with open(nombre_archivo_nuevo, 'w', newline='') as csvnewfile:
        writer = csv.writer(csvnewfile, delimiter=' ',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        while alumnos_leidos != "":
            for grupo in range(grupos_creados):
                count = 0
                while count < alumnos_por_grupo:
                    row = rdm.choice(alumnos_leidos)
                    writer.writerow(f"{row}\tGrupo: {grupo+1}")
                    alumnos_leidos.remove(row)
                    count+=1
except Exception as ex:
    print(ex) 