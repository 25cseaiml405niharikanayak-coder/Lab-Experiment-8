import numpy as np


a = np.array([1, 2, 3], dtype=np.int32)
b = np.array([1.5, 2.5, 3.5], dtype=np.float64)
c = np.array([True, False, True], dtype=bool)
d = np.array(["A", "B", "C"], dtype=str)

print("Integer array:", a)
print("Data type:", a.dtype)

print("Float array:", b)
print("Data type:", b.dtype)

print("Boolean array:", c)
print("Data type:", c.dtype)

print("String array:", d)
print("Data type:", d.dtype)


one_d = np.array([1, 2, 3])
two_d = np.array([[1, 2], [3, 4]])
three_d = np.array([[[1, 2], [3, 4]]])

print("\n1-D Array:")
print(one_d)

print("\n2-D Array:")
print(two_d)

print("\n3-D Array:")
print(three_d)
