from flask import Blueprint, jsonify
import csv

UPLOAD_FOLDER = 'uploads'

main = Blueprint('download_file_blueprint', __name__)

@main.route('/', methods=['GET', 'POST'])
def download_files(id):
    try:
        content = []
        with open(f"{UPLOAD_FOLDER}/{id}", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                content.append(row)
        return jsonify(content)
    except Exception as ex:
        return jsonify("Archivo no encontrado") 