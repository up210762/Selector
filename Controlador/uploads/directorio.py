import os

with os.scandir() as ficheros:
	ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]

print(ficheros)
