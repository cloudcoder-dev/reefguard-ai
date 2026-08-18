import tensorflow as tf

print("Starting program...")

print("TensorFlow Version:", tf.__version__)

# Shortcut so we can write layers.Conv2D instead of tf.keras.layers.Conv2D
layers = tf.keras.layers

print("Building CNN model...")

# Build the model
model = tf.keras.Sequential([

    # Input Layer
    layers.Input(shape=(224, 224, 3)),

    # First Convolution Layer
    layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        activation="relu"
    ),

    # Max Pooling Layer
    layers.MaxPooling2D(pool_size=(2, 2)),

    # Flatten Layer
    layers.Flatten(),

    # Hidden Dense Layer
    layers.Dense(
        units=64,
        activation="relu"
    ),

    # Output Layer
    layers.Dense(
        units=2,
        activation="softmax"
    )
])
# ✅ Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


print("Model built successfully!")

print("\n========== MODEL SUMMARY ==========\n")
model.summary()
print("\n===================================\n")

print("Program finished successfully!")