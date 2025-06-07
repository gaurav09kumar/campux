import numpy as np

a1 = np.random.random((3,3))
print(a1)

print("----------------------------------------")

a2 = np.round(a1 * 100)
print(a2)

print("----------------------------------------")

# max , min, sum, prod
print(np.max(a2), np.min(a2), np.sum(a2), np.prod(a2), sep = "\n\n")

print("----------------------------------------")
# minimum from row wise
print(np.min(a2, axis=1))
# minum from column wise
print(np.min(a2, axis=0))
print("----------------------------------------")

# mean/median/std/var
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

print("----------------------------------------")

# trignometric
print(np.sin(a1))
print(np.cos(a1))
print(np.tan(a1))

print("----------------------------------------")
# dot product - two matrix are 3,4 and 4,3 the O/P is 3,3
# 3,5 3,5 then no dot product
a3 = np.arange(12).reshape(3,4)
a4 = np.arange(12, 24).reshape(4,3)
print(a3, a4, sep='\n')
print(np.dot(a3, a4))

print("----------------------------------------")

# log and exp functions
print(np.log(a1) , np.exp(a1), sep = '\n\n')

print("----------------------------------------")

np_array_float_data = np.random.random((2,3))*100
print(np_array_float_data, end = "\n\n")

print(np.round(np_array_float_data))
print(np.floor(np_array_float_data))
print(np.ceil(np_array_float_data))

print("----------------------------------------")
