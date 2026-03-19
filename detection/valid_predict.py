import tensorflow as tf

model = tf.keras.models.load_model("parking_model.h5")

dataset_path = r"D:\parking-space-detection-prediction\detection\dataset\valid"

val = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    image_size=(224,224),
    batch_size=32
)

loss, accuracy = model.evaluate(val)

print(f"Validation Accuracy: {accuracy * 100:.2f}%")