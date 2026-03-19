import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load trained model
model = tf.keras.models.load_model("parking_model.h5")

# Path of test image (CHANGE THIS)
img_path = r"D:\parking-space-detection-prediction\test.jpg"

# Load image
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Normalize
img_array = img_array / 255.0

# Prediction
prediction = model.predict(img_array)

# Output
if prediction[0][0] > 0.5:
    print("🚗 Parking Spot is OCCUPIED")
else:
    print("🅿 Parking Spot is EMPTY")
    