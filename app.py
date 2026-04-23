from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files['file']

        if file.filename == "":
            return "No file selected"

        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

       if "ai" in file.filename.lower():
          result = "Fake Image"
      else:
          result = "Real Image"
      return render_template("index.html", prediction=result)

    except Exception as e:
        return f"Error: {str(e)}"

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
