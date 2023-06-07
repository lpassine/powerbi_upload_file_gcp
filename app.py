from flask import Flask, render_template, request
import os

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def home():
    return "Welcome to CSV Upload"

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Retrieve the uploaded file
        csv_file = request.files["file"]

        # Save the file to a secure location
        file_path = "/Users/larissapassine/Documents/Loreal/Projects Files/Luxe Forecast/" + csv_file.filename
        csv_file.save(file_path)

        # Process the uploaded file (e.g., trigger script execution)

        return "File uploaded successfully"

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)

