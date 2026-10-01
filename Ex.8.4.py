import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Statistical operations
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Sum:", np.sum(arr))

# Broadcasting
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

print("\nArray A:")
print(a)

print("\nArray B:")
print(b)

# Broadcasting B to each row of A
result = a + b

print("\nResult after Broadcasting:")
print(result)
