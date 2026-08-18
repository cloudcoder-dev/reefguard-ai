import tensorflow as tf
import numpy as np
import os

# Load the trained model
model = tf.keras.models.load_model("coral_model.keras")

# Class names
class_names = ["Bleached", "Healthy"]

# Folder containing sample images
sample_folder = "dataset/sample_images"

# Go through every image in the folder
for filename in os.listdir(sample_folder):

    # Only process image files
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(sample_folder, filename)

        # Load and resize image
        image = tf.keras.utils.load_img(
            image_path,
            target_size=(224, 224)
        )

        # Convert image to numbers
        image_array = tf.keras.utils.img_to_array(image)

        # Add batch dimension
        image_array = tf.expand_dims(image_array, axis=0)

        # Make prediction
        prediction = model.predict(image_array, verbose=0)

        # Find predicted class
        predicted_class = np.argmax(prediction)

        # Get confidence
        confidence = prediction[0][predicted_class] * 100

        # Print result
        print("--------------------------------")
        print("Image:", filename)
        print("Prediction:", class_names[predicted_class])
        print(f"Confidence: {confidence:.2f}%")

                # Local fallback explanation
        if class_names[predicted_class] == "Healthy":
            explanation = (
                f"The computer vision model classified the coral as Healthy "
                f"with {confidence:.2f}% confidence. "
                f"This suggests the coral may be in relatively good condition."
            )
        else:
            explanation = (
                f"The computer vision model classified the coral as Bleached "
                f"with {confidence:.2f}% confidence. "
                f"This suggests the coral may be experiencing bleaching or stress."
            )

        print("Explanation:", explanation)
        print(
            "Note: This is an AI-assisted screening result "
            "and should be verified by a marine or environmental expert."
        )
