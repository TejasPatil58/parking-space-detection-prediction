
import tensorflow as tf
import os
from tensorflow.keras import layers, models


# DATASET PATH

dataset_path = r"D:\parking-space-detection-prediction\detection\dataset"

train_dir = os.path.join(dataset_path, "train")
val_dir = os.path.join(dataset_path, "valid")

# LOAD DATASET

train = tf.keras.preprocessing.image_dataset_from_directory(
    train_dir,
    image_size=(224, 224),
    batch_size=32
)

val = tf.keras.preprocessing.image_dataset_from_directory(
    val_dir,
    image_size=(224, 224),
    batch_size=32
)


# NORMALIZE DATA (0-255 → 0-1)

train = train.map(lambda x, y: (x / 255.0, y))
val = val.map(lambda x, y: (x / 255.0, y))


# BUILD CNN MODEL

model = models.Sequential([

    # 1st Convolution Block
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D(),

    # 2nd Convolution Block
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    # 3rd Convolution Block
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(),

    # Flatten
    layers.Flatten(),

    # Fully Connected Layers
    layers.Dense(128, activation='relu'),
    layers.Dense(1, activation='sigmoid')   # Binary output
])


# COMPILE MODEL

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)


# TRAIN MODEL

history = model.fit(
    train,
    validation_data=val,
    epochs=5
)


# SAVE MODEL

model.save("parking_model.h5")
print("Model Saved Successfully!")