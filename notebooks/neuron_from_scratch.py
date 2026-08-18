# Inputs (features)
color = 0.9
texture = 0.4
shape = 0.2

# Weights
w1 = 0.8
w2 = 0.3
w3 = 0.1

# Bias
bias = 0.2

# Neuron calculation
output = (color * w1) + (texture * w2) + (shape * w3) + bias

print("Neuron output:", output)