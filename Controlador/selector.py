from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import random as rdm
import csv, os

app = Flask(__name__)
CORS(app, resources={r"/upload":{"origins": "*"}})

app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = 'csv'

def allowed_file(filename):
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS#'.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS, 

@app.route('/upload', methods=['POST'])
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
                with open(f"{app.config['UPLOAD_FOLDER']}/{nombre_archivo}", newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        alumnos_leidos.append(row)
                with open(f"{app.config['UPLOAD_FOLDER']}/{nombre_archivo_nuevo}.csv", 'w', newline='') as csvnewfile:
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
                                    alumnos_leidos.remove(row)
                                except Exception as ex:
                                    return jsonify("Archivo listo")
            return jsonify("Archivo no permitido")
    except Exception as ex:
        return jsonify(f"Error: {ex}")
if __name__ == '__main__':
    app.run(debug=True)