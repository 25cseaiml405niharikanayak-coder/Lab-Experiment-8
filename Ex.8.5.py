import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50])

# Save the array
np.save("my_array.npy", arr)

print("Array saved successfully.")

# Load the array
loaded_arr = np.load("my_array.npy")

print("Loaded Array:")
print(loaded_arr)
