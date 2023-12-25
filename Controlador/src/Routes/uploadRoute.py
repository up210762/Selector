from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from src.Modelos.allowed_file import allowed_file
import random as rdm
import csv, os

UPLOAD_FOLDER = 'uploads'

main = Blueprint('upload_file_blueprint', __name__)

@main.route('/', methods=['GET','POST'])
def upload():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return jsonify('No hay fragmento de archivo')
            file = request.files['file']

            if file.filename == '':
                return jsonify('No hay archivo seleccionado')
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
            if file and allowed_file(file.filename):
                nombre_archivo = file.filename
                nombre_archivo_nuevo = request.form['txt-new-name']
                grupos_creados = int(request.form['txt-groups'])
                alumnos_por_grupo = int(request.form['txt-alumnos-grupo'])
                alumnos_leidos = []
                datos_tabla = []
                with open(f"{UPLOAD_FOLDER}/{nombre_archivo}", newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        alumnos_leidos.append(row)
                with open(f"../Vista/uploads/{nombre_archivo_nuevo}.csv", 'w', newline='') as csvnewfile:
                    writer = csv.writer(csvnewfile, delimiter=' ',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                    row = []
                    while alumnos_leidos != "":
                        for grupo in range(grupos_creados):
                            count = 0
                            while count < alumnos_por_grupo:
                                try: 
                                    alumno = rdm.choice(alumnos_leidos)
                                    
                                    row.append([alumno[0], alumno[1],f"Grupo: {grupo+1}"])
                                    writer.writerow([f"{alumno[0]}, {alumno[1]}, Grupo: {grupo+1}"])
                                    count+=1
                                    alumnos_leidos.remove(alumno)
                                except Exception as ex:
                                    return jsonify(row)
            return jsonify("Archivo no permitido")
        else:
            return jsonify('Método no permitido.')
    except Exception as ex:
        return jsonify(f"Error: {ex}")