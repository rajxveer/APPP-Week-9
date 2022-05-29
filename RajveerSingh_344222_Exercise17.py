import numpy as np

a = np.array([[10, 30], [20, 60]])

print("\nArray a:\n", a)

print("\nPrint mean for each column:\n", a.mean(axis = 0))

print("\nPrint mean for each row:\n", a.mean(axis = 1))