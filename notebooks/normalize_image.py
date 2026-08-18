from PIL import Image
import numpy as np

# Load image
image = Image.open("dataset/sample_images/Coral.jpg")

# Convert to NumPy array
image_array = np.array(image)

print("Before normalization:")
print("Data type:", image_array.dtype)
print("Min value:", image_array.min())
print("Max value:", image_array.max())

# Normalize
normalized = image_array / 255.0

print("\nAfter normalization:")
print("Data type:", normalized.dtype)
print("Min value:", normalized.min())
print("Max value:", normalized.max())