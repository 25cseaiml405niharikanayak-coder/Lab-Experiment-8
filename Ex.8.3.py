import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Array:")
print(arr)

# Array properties
print("\nNumber of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Item size:", arr.itemsize)

# NumPy functions
print("\nMaximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))

# Reshape
print("\nReshaped Array:")
print(arr.reshape(3, 2))

# Flatten
print("\nFlattened Array:")
print(arr.flatten())
