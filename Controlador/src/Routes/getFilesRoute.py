from flask import Blueprint, jsonify, request
import os

main = Blueprint('get_files_blueprint', __name__)

@main.route('/', methods=['GET', 'POST'])
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