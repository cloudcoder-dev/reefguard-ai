import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# Load the trained model
model = tf.keras.models.load_model("coral_model.keras")

# Test dataset
test_folder = "dataset/Coral Reef Images/test"

# Load test images
test_data = tf.keras.utils.image_dataset_from_directory(
    test_folder,
    image_size=(224, 224),
    batch_size=32,
    shuffle=False
)

# Class names
class_names = test_data.class_names

print("Classes:", class_names)

# Get predictions
predictions = model.predict(test_data, verbose=0)

# Convert model probabilities into predicted classes
predicted_classes = np.argmax(predictions, axis=1)

# Get actual classes
actual_classes = np.concatenate(
    [labels.numpy() for images, labels in test_data],
    axis=0
)

# Print classification report
print("\nClassification Report:")
print(
    classification_report(
        actual_classes,
        predicted_classes,
        target_names=class_names
    )
)

# Print confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(actual_classes, predicted_classes))