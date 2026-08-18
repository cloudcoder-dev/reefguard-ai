import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

print("Number of GPUs Available:", len(tf.config.list_physical_devices('GPU')))

print("Hello TensorFlow!")