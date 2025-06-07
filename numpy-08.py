import numpy as np

"""
The term broadcasting describes how numpy treats arrays with different shapes during arithmetic operations
The smaller array is "broadcast" across the larger array so thay they have compatible shapes
"""


a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
print(b)
print(a+b)

# addition with different type of array shape 
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)

print(a)
print(b)
print(a+b) # Two different shapes will also be added - This is broadcasting


"""
(3,2) is 2D and (3,) is 1D so first add 1 in head - (1,3) 
(3,3,3) is 3D and (3,) is 1D so first add 1 in head - (1,1,3)

Now make the (1,1,3) to (3,3,3) so that both arrays shape match with one another

If there is a dimension whose size is not 1  in either of two arrays, it cannot be broadcasted and error is raised

"""
print("--------------------"*2)

#More examples
a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
print(b)
print("--------------------"*2)
print(a+b)
print("--------------------"*2)

#More examples
a = np.arange(12).reshape(3,4)
b = np.arange(3)

print(a)
print(b)
# print(a+b) # This will throw an error 
# Value Error - operands could not be broadcasted together with shapes (3,4) (3,)
print("--------------------"*2)
#More examples
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1) # Here extend both the 1 to the 3,3
# broadcasting will work here

print(a)
print("--------------------"*2)
print(b)

print("--------------------"*2)
print(a+b)
print("--------------------"*2)

a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)
# broadcasting will work here

print(a)
print("--------------------"*2)
print(b)

print("--------------------"*2)
print(a+b)
print("--------------------"*2)

a = np.array([1])
# shape -> 1,1
b = np.arange(4).reshape(2,2)
# shape -> (2,2)

print(a)
print(b)
print("--------------------"*2)
print(a+b)
print("--------------------"*2)


a = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
print(a)
print(b)
#print(a+b) # This will throw Value Error
# because both the dimensions are same and there is no 1 in any of the index shape
# So broadcasting wont be possible
print("--------------------"*2)


a = np.arange(16).reshape(4,4)
b = np.arange(4).reshape(2,2)
print(a)
print(b)
print(a+b)

"""
The concept of broadcasting in numpy is to add two non matching shape arrays if they follow some set of rules. It is used in a technique called vectorization.
Numpy internally avoids loops, and came up with a topic called as vectorization.
"""
