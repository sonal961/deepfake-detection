import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("model/deepfake-detection-model.h5")

def predict_image(image_path):
    img = Image.open(image_path).resize((128, 128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)


    if prediction[0][0] > 0.5:
        return "Fake Image"
    else:
        return "Real Image"
