import numpy as np

a1 = np.random.random((3,3))
print(a1)

print("----------------------------------------")

a2 = np.round(a1 * 100)
print(a2)

print("----------------------------------------")

# INDEXING AND SLICING

a3 = np.arange(12).reshape(3,4)
a4 = np.arange(8).reshape(2,2,2)

a5 = np.arange(10)

print(a3, a4, a5, sep="\n\n")

print(a5[-1])
print(a5[3])
print("----------------------------------------")

#2D -  row,column for a specific element
print(a3[1,2])

print("----------------------------------------")
#3D - in which 2d array does 5 belong - 1 - then first row second column
print(a4[1,0,1])
print(a4[0,1,0])
print(a4[0,0,0])
print(a4[1,1,0])


print("----------------------------------------")
# indexing is done for the single element
# with slicing we can get multiple element


print(a5[2:5:2])
print(a3[0,:]) # first row and all the columns
print(a3[:,2]) # if you need 3rd columns

print(a3[1:,1:3]) # need 5 6 9 10
# 0 8 3 11

print(a3[::2,::3])

# 1 3 9 11
print(a3[::2,1::2])

# 4 7
print(a3[1,::3])

# 1 2 3 5 6 7
print(a3[:2,1::])

print("----------------------------------------")
a6 = np.arange(27).reshape(3,3,3)
print(a6)
print("----------------------------------------")
# the above 3d array has 3 - 2d arrays. If we want the second 2d array
print(a6[1]) 
print("----------------------------------------")
print(a6[::2])
print("----------------------------------------")
print(a6[0,1,:])
print("----------------------------------------")
print(a6[1,2,1])
print("----------------------------------------")
print(a6[1,:,1])
print("----------------------------------------")
print(a6[2,1:,1:])
print("----------------------------------------")
print(a6[0:3:2,0,0::2])
print("----------------------------------------")
print(a6[::2,0,::2])
print("----------------------------------------")

# Iterating - using loops
print(a5, a3, sep="\n\n")

for i in a5:
    print(i)
print("----------------------------------------")
for i in a3:
    print(i)
print("----------------------------------------")

for i in a3:
    for j in i:
        print(j)

print("----------------------------------------")

# using np nditer function - to print all items of any dimension

for i in np.nditer(a3):
    print(i)
    
print("Reshaping ----------------------------------------")

# Reshaping - 
"""
Three functions - 
    reshape
    Transpose - row to column and column to row
    ravel - any dimension of np array to 1D
"""

print(a2)
print("Transpose : \n", np.transpose(a2))
print("Transpose : \n", a2.T) # syntax 2

print("Ravel : \n", a2.ravel())
print("Ravel : \n", a3.ravel())

print("----------------------------------------")


# Stacking -  Add 2 or more np arrays
"""
Stacking can be done in 2 ways - 
    Horizontal Stacking -->
        [2 X 2] [2 X 2] arrays --> [2 X 4] 2 rows and 4 colums array
    Vertical Stacking
        [2 X 2] [2 X 2] --> [4 X 2] 4 rows and 2 colums array
        
Now where will this get used - 
Suppose you have same data from multiple data sources - Data from db, api, other sources
You can combine them for further analysis

Note - for stacking - shape has to be same else, it wont work
"""

a7 = np.arange(4).reshape(2,2)
a8 = np.arange(4).reshape(2,2)


print(a7, a8 , sep = "\n\n")

horizontal_stacking = np.hstack((a7,a8))
vertical_stacking =  np.vstack((a7,a8))
print("Horizontal Stacking : \n", horizontal_stacking , "shape : ", np.shape(horizontal_stacking) , end="\n\n")
print("Vertical Stacking : \n", vertical_stacking , "shape : " , np.shape(vertical_stacking) , end="\n\n")


# Splitting - 
"""
Just the opposite of stacking - 
[ ] Suppose this is an array - horizontal split will result in 2 new arrays [ | ]
vertical split will result [-]

We can split equal division only

Usecase - THere is an entire college data and you want to separate a specific branch data

hstack no of rows should be same. and for vstack no of col should be same.

"""

print(a7, a8 , sep = "\n\n")

horizontal_split = np.hsplit(a7, 2) # divide a7 in 2 equal parts
vertical_split = np.vsplit(a7, 2) # divide a7 in 2 equal parts vertically
print("Horizontal Split : \n", horizontal_split , "shape : ", "\n", np.shape(horizontal_split) , end="\n\n")
print("Vertical Split : \n", vertical_split , "shape : ","\n",  np.shape(vertical_split) , end="\n\n")
