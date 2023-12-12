from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import random as rdm
import csv, os

app = Flask(__name__)
CORS(app, resources={
    r"/upload":{"origins": "*"},
    r"/getfiles":{"origins": "*"},
    r"/uploads/*":{"origins": "*"}
    })

app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = 'csv'

def allowed_file(filename):
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS#'.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS, 

def mostrar_contenido_csv(archivo_csv):
    filas = []
    with open(archivo_csv, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)

        # Lee el contenido
        for fila in lector_csv:
            filas.append(fila)
        return fila

@app.route('/upload', methods=['GET','POST'])
def upload():
    try:
        if request.method == 'POST':
            if 'file' not in request.files:
                return jsonify('No hay fragmento de archivo')
            file = request.files['file']

            if file.filename == '':
                return jsonify('No hay archivo seleccionado')
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            if file and allowed_file(file.filename):
                nombre_archivo = file.filename
                nombre_archivo_nuevo = request.form['txt-new-name']
                grupos_creados = int(request.form['txt-groups'])
                alumnos_por_grupo = int(request.form['txt-alumnos-grupo'])
                alumnos_leidos = []
                datos_tabla = []
                with open(f"{app.config['UPLOAD_FOLDER']}/{nombre_archivo}", newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        alumnos_leidos.append(row)
                with open(f"../Vista/uploads/{nombre_archivo_nuevo}.csv", 'w', newline='') as csvnewfile:
                    writer = csv.writer(csvnewfile, delimiter=' ',
                                        quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                    while alumnos_leidos != "":
                        for grupo in range(grupos_creados):
                            count = 0
                            while count < alumnos_por_grupo:
                                try: 
                                    row = rdm.choice(alumnos_leidos)
                                    writer.writerow(f"{row}\tGrupo: {grupo+1}")
                                    count+=1
                                    datos_tabla.append([row,f"Grupo: {grupo+1}"])
                                    alumnos_leidos.remove(row)
                                except Exception as ex:
                                    return jsonify(datos_tabla)
            return jsonify("Archivo no permitido")
        else:
            return jsonify('Método no permitido.')
    except Exception as ex:
        return jsonify(f"Error: {ex}")
    
@app.route('/getfiles', methods=['GET', 'POST'])
def get_files():
    try:
        if request.method == 'GET':
            with os.scandir('../Vista/uploads') as ficheros:
                ficheros = [fichero.name for fichero in ficheros 
                            if fichero.is_file() 
                            and fichero.name.endswith('.csv')]
                return jsonify(ficheros)
        else:
            return jsonify('Método no permitido.')
    except Exception as ex:
        return ('Error')

@app.route('/uploads/<id>', methods=['GET', 'POST'])
def download_files(id):
    try:
        content = []
        with open(f"{app.config['UPLOAD_FOLDER']}/{id}", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                content.append(row)
        return jsonify(content)
    except Exception as ex:
        return jsonify("Archivo no encontrado")

if __name__ == '__main__':
    app.run(debug=True)