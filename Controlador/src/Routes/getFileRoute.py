from flask import Blueprint, request, jsonify
import csv

main = Blueprint("get_file_blueprint", __name__)

@main.route('/', methods=['GET', 'POST'])
def get_file(id):
    try:
        alumnos_leidos = []
        if request.method == 'GET':
            with open(f"../Vista/uploads/{id}", newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        alumnos_leidos.append([row[0], row[1], row[2]])
                        print(row)
            return jsonify(alumnos_leidos)
        else:
            return jsonify('Método no permitido.')
    except Exception as ex:
        return ('Error')   