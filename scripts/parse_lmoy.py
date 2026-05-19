import numpy as np

filename = "lmoy0002"

data = np.loadtxt(filename)

x = data[:, 0]
y = data[:, 1]

average_displacement = np.mean(y)

print("Average displacement:", average_displacement)
