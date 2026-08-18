from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

#load image
image = Image.open("dataset/sample_images/Coral.jpg")
# Convert to NumPy array
image_array = np.array(image)

#print the information
#print("Type:", type(image_array))
#print("Shape:", image_array.shape)
#print("Data type:", image_array.dtype)

 # Access one pixel
#pixel = image_array[100, 100]

#print("Pixel value:", pixel)
#print("Red:", pixel[0])
#print("Green:", pixel[1])
#print("Blue:", pixel[2])

#print("Top-left pixel:", image_array[0, 0])
#print("Center pixel:", image_array[300, 235])
#print("Bottom-right pixel:", image_array[599, 470])

#stage 3

# Make image brighter
bright_image = np.clip(image_array + 50, 0, 255)

# Display
plt.imshow(bright_image)
plt.axis("off")
plt.show()