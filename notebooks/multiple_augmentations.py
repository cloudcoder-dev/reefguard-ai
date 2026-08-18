from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Load image
image = Image.open("dataset/sample_images/Coral.jpg")

# Augmentations
flip = image.transpose(Image.FLIP_LEFT_RIGHT)
rotate = image.rotate(30)
bright = ImageEnhance.Brightness(image).enhance(1.5)

# Display
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(flip)
plt.title("Flip")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(rotate)
plt.title("Rotate")
plt.axis("off")

plt.subplot(2,2,4)
plt.imshow(bright)
plt.title("Bright")
plt.axis("off")

plt.show()