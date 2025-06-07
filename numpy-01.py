import numpy as np

"""
NumPy is a general-purpose array-processing package. 
It provides a high-performance multidimensional array object, 
    and tools for working with these arrays. 
It is the fundamental package for scientific computing with Python. 
Numpy is basically used for creating array of n dimensions.
"""
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

# nd array with float data
d = np.array([1.0, 2.0, 3.0]) # 1-D Array
print(d, type(d))
print("------------------------------------------------")

# nd array with bool data
d = np.array([0, 1, 2, 3],dtype=bool) # 1-D Array
print(d, type(d))
print("------------------------------------------------")

# nd array with bool data
d = np.array([0, 1, 2, 3],dtype=complex) # 1-D Array
print(d, type(d))
print("------------------------------------------------")

# arange functions
"""
numpy.arange() function creates an array of evenly spaced values within a given interval. 
It is similar to Python's built-in range() function but returns a NumPy array instead of a list.
"""
e = np.arange(1, 11)
print(e, type(e))
print("------------------------------------------------")

# with step
# Creating a sequence of floating-point numbers from 0 to 1 
# with a step size of 0.2 using np.arange()
sequence = np.arange(0, 1, 0.2)
print("Floating-Point Sequence:", sequence) 

print("------------------------------------------------")

#reshape
reshaped = np.arange(1, 11).reshape(2, 5)
print(reshaped)

print("------------------------------------------------")
reshaped = np.arange(1, 10).reshape(3, 3)
print(reshaped)

print("------------------------------------------------")

# create numpy array with all elements as 0 or 1
# these will be useful - during model initialization, data padding/masking
all_zero = np.zeros(10)
print(all_zero)

all_one = np.ones(5)
print(all_one, type(all_one))

# provide tuple as input
all_zeros = np.zeros((2, 3))
print(all_zeros)

all_ones = np.ones((4, 5))
print(all_ones, type(all_ones))

print("------------------------------------------------")
"""
numpy.random.random() is one of the function for doing random sampling in numpy. 
It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0)
"""
np_random = np.random.random(size=(3,4))
print(np_random)
print("------------------------------------------------")

# np.linspace - linear space - from start to end give equal spaced elements
# linear spaced elments in a given range
linspace_ = np.linspace(-10,10,10)
print(linspace_)

print("------------------------------------------------")

# identity matrix whose diagonal elements will be 1 and other elements are 0
identity_matrix = np.identity(3)
print(identity_matrix)

print("------------------------------------------------")
