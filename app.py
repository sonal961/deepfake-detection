from flask import Flask, render_template, request
import os
from detect import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    print("PREDICT FUNCTION CALLED")

    if 'file' not in request.files:
        print("No file uploaded")
        return "No file uploaded"

    file = request.files['file']

    if file.filename == "":
        print("No file selected")
        return render_template("index.html", prediction="No file selected")

    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    print("File saved at:", path)

    result = predict_image(path)
    print("Prediction:", result)

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)