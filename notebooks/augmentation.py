from PIL import Image
import matplotlib.pyplot as plt

# Load image
image = Image.open("dataset/sample_images/Coral.jpg")

# Flip horizontally
flipped = image.transpose(Image.FLIP_LEFT_RIGHT)

# Show original
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

# Show flipped
plt.subplot(1,2,2)
plt.imshow(flipped)
plt.title("Flipped")
plt.axis("off")

plt.show()