from PIL import Image
import matplotlib.pyplot as plt

# Load image
image = Image.open("dataset/sample_images/Coral.jpg")

# Resize image
resized = image.resize((224, 224))

# Display
plt.imshow(resized)
plt.axis("off")
plt.show()

# Print sizes
print("Original Size:", image.size)
print("Resized Size:", resized.size)