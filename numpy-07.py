import numpy as np

# Fancy indexing -> Usecases where in a dataset you need specific rows and columns
# Boolean indexing

a = np.arange(12).reshape(4,3)
print(a)

# Now we want 0th row, 2,3rd rows
# this cant be achieved with normal indexing

print("----------------------------")
print(a[[0,2,3]]) # provide a list with the required row index 

print("----------------------------")

b = np.arange(24).reshape(6,4)
print(b)

print("----------------------------")

print(b[[0,2,3,5]])

print("----------------------------")

# 1st 2nd and 3rd columns
print(b[:,[0,2,3]])
print("----------------------------\n"*2)


# Boolean indexing - give the items from an array which are even based on condition

rand_array = np.random.randint(1,100,24).reshape(6,4)
print(rand_array)
print(rand_array > 50) # This is called a boolean array - because each element inside this is either True or False

# We can use this as a boolean mask and do the filtering  (best to use when filter the data based on a given condition)

print(rand_array[rand_array > 50]) # Only the items will remain where True and False will be removed

print("----------------------------\n"*2)

print(rand_array[rand_array % 2 == 0]) # Filter the numbers divisible by 2 nparray[index has condition]

print(rand_array[(rand_array > 50) & (rand_array % 2 == 0)]) # We used bitwise and because we are working with boolean data
