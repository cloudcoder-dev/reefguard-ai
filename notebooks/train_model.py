import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

print("Loading dataset...")

# Load dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/Coral Reef Images/train",
    image_size=(224, 224),
    batch_size=32
)
print("Dataset loaded successfully!")

valid_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/Coral Reef Images/valid",
    image_size=(224, 224),
    batch_size=32
)
print("Train classes:", train_dataset.class_names)
print("Validation classes:", valid_dataset.class_names)
print("Validation dataset loaded successfully!")



# Build CNN
model = tf.keras.Sequential([

    layers.Input(shape=(224, 224, 3)),

    layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu"
    ),

    layers.MaxPooling2D(pool_size=(2, 2)),

    layers.Flatten(),

    layers.Dense(64, activation="relu"),

    layers.Dense(2, activation="softmax")

])

print("CNN built!")

# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("Model compiled!")

# Train model
#history = model.fit(
    #train_dataset,
    #epochs=5
#)
history = model.fit(
    train_dataset,
    validation_data=valid_dataset,
    epochs=5
)

print("Training Complete!")

# Save model
#model.save("../coral_model.keras")
model.save("coral_model.keras")

print("Model saved successfully!")
# Plot Accuracy

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

plt.legend(["Training Accuracy", "Validation Accuracy"])

plt.show()

# Plot Lossplt.figure()
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(["Training Loss","Validation Loss"])
plt.show()