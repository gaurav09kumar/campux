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

# ARRAY OPERATIONS

# changing datatype - we can use when we think that a particular data can be reduced to a lower level
print(a.dtype)
a = a.astype(np.int32)
print(a, a.dtype)

print("------------------------------------------------")

# scalar operations - we can use all arithmetic operators 
print(b, b * 2, b**2 , sep = '\n')

print("------------------------------------------------")

# relational - we can use all relational operations

print(b>=5)
print("------------------------------------------------")

# vector operations - between twon numpy arrays
a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(11,21,dtype=np.int32)
print(a1, a2 , sep = '\n\n')
print(a1 + a2)
print(a1 ** a2)




