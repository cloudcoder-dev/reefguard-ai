import tensorflow as tf

train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/Coral Reef Images/train",
    image_size=(224, 224),
    batch_size=32
)

print("Class names:", train_dataset.class_names)