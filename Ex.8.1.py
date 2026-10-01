import numpy as np

a = np.array([10,20,30,40,50])

print("Array:", a)
print("Type:", type(a))

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

print("Elements from 0-4 index:", a[1:5])

names = np.array(["Alice", "Bob", "Charlie", "David"])

print("String Array:", names)
print("First name:", names[0])
print("Last name:", names[-1])
