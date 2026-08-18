import tensorflow as tf
import matplotlib.pyplot as plt

# Load dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    "dataset/Coral Reef Images/train",
    image_size=(224, 224),
    batch_size=32
)

# Take one batch
for images, labels in train_dataset.take(1):

    print("Images shape:", images.shape)
    print("Labels shape:", labels.shape)

    plt.figure(figsize=(8, 8))

    for i in range(4):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(train_dataset.class_names[labels[i]])
        plt.axis("off")

    plt.show()