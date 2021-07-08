
import os
from os import environ
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, jsonify


import warnings
warnings.filterwarnings("ignore")
# Werkzeug is a utility library for WSGI. WSGI itself is a protocol or convention that ensures that 
# your web application can speak with the webserver and more importantly that web applications work nicely together.
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_LOCATION = environ.get('UPLOAD_LOCATION')
# app.secret_key = b'_5#yi4L"F4w8z\n\xec]?'

# file size limit
# app.config['MAX_CONTENT_LENGTH'] = int(51200e6) # 50GB


class UploadVideo:

    def __init__(self):
        # file storage location
        self.main_path = str(UPLOAD_LOCATION)
        self.ALLOWED_EXTENSIONS = {'mp4'}

    

    def allowed_file(self,file_name):

        """Checks the extension and returns True if correct"""
        #print(file_name)
        file_present = None
        file_present = file_name.split('.')[1] in self.ALLOWED_EXTENSIONS
        return file_present

    def upload_file(self):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            print("File Name",file.filename)
            if file.filename == '':
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": "Please select the video file",
                    "aividStatusCode": 101
                }
                return jsonify(resp)
            # if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if self.allowed_file(filename):
                file.save(os.path.join(self.main_path, filename))
                resp = {
                    "status": True,
                    "reasonPhrase": "OK",
                    "statusCode": 200,
                    "error": None,
                    "aividStatusCode": 110
                }
                return jsonify(resp)
            else:
                resp = {
                    "status": False,
                    "reasonPhrase": "OK",
                    "statusCode": 422,
                    "data": [],
                    "error": "Invalid file!.... File should be in .mp4 format",
                    "aividStatusCode": 106
                }
                return jsonify(resp)
            
        return '''
        <!doctype html>
        <title>Upload Video</title>
        <h1>Upload Video</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''


# if __name__ == '__main__':
# 	app.run(debug=True)


