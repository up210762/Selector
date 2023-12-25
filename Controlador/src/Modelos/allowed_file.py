ALLOWED_EXTENSIONS = 'csv'

def allowed_file(filename):
    return filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS#'.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS, 
