import numpy as np

# create numpy array
a = np.array([1, 2, 3]) # 1-D Array
print(a, type(a))
print("------------------------------------------------")

# 2D - 2 rows and 3 columns
b = np.array([[1, 2, 3],[4, 5, 6]])
print(b, type(b))
print("------------------------------------------------")

# 3D
c = np.array([[[1, 2],[3, 4 ], [5, 6]]])
print(c, type(c))
print("------------------------------------------------")

# ndim - to check the number of dimensions of the nd array
print("dimensions: ",a.ndim, b.ndim, c.ndim, sep='\n')

print("------------------------------------------------")

# shape - it says how many rows and columns are present in nd array
# for 3d shape - it says number of 2d array, number of rows and columns of 2d array
print("shape: ", a.shape, b.shape, c.shape, sep = '\n')

print("------------------------------------------------")

#size - number of elements in each nd array 
print("size: ", a.size, b.size, c.size, sep = '\n')

print("------------------------------------------------")

#item size - each item occupies how much memory
# int 64 takes - 8 bytes
# int 32 takes - 4 bytes
print("item size: ",a.itemsize, b.itemsize, c.itemsize, sep = '\n')

print("------------------------------------------------")

#data type
print("data type: ",a.dtype, b.dtype, c.dtype, sep = '\n')

print("------------------------------------------------")
