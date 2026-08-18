from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("../dataset/sample_images/Coral.jpg")

print("Width, Height:", image.size)
print("Mode:", image.mode)

pixel = image.getpixel((100, 100))
print("Pixel at (100,100):", pixel)

plt.imshow(image)
plt.axis("off")
plt.show()