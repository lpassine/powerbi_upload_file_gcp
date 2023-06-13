import os
from flask import Flask, render_template, request
from google.cloud import storage

app = Flask(__name__)

# Set the path to your Google Cloud Storage credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/pb-integration-389120-e02e7b60859f.json"

@app.route('/')
def home():
    return "Welcome to File Upload"

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['file']

        # Upload the file to Google Cloud Storage
        client = storage.Client()
        bucket = client.get_bucket('power-bi-data-integration')  
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)

        return "File uploaded successfully!"

    return render_template("upload.html")

# Add the following configuration for Google Cloud App Engine
# to use the main() function as the entry point of the application.
def main():
    # Run the Flask app
    app.run()

if __name__ == '__main__':
    main()
