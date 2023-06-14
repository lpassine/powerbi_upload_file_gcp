import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from google.cloud import storage

app = Flask(__name__)

# Set the path to your Google Cloud Storage credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/pb-integration-389120-e02e7b60859f.json"
os.environ['API_KEY'] = 'AIzaSyAjFkdPM9Pspl7Rj-Lc0hVcwigzUDB1__c'

@app.route('/')
def home():
    return "Welcome to File Upload"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file found in the request"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        # Upload the file to Google Cloud Storage
        client = storage.Client()
        bucket = client.get_bucket('power-bi-data-integration')
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)

        return "File uploaded successfully!"

    return render_template("upload.html")

@app.route('/proxy-upload', methods=['GET', 'POST'])
def proxy_upload():
    if request.method == 'POST':
        req = request.environ.get('HTTP_X_FORWARDED_PROTO', request.scheme)
        url = req + '://' + request.host + '/upload'
        return redirect(url, code=307)
    elif request.method == 'GET':
        return redirect(url_for('upload'))
    else:
        return "Method not allowed"

# Add the following configuration for Google Cloud App Engine
# to use the main() function as the entry point of the application.
def main():
    # Run the Flask app
    app.run()

if __name__ == '__main__':
    main()

