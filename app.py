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
    try:
        if 'file' not in request.files:
            return "No file uploaded"

        file = request.files['file']

        if file.filename == "":
            return "No file selected"

        path = os.path.join("static", file.filename)
        file.save(path)

        result = predict_image(path)

        return render_template("index.html", prediction=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
