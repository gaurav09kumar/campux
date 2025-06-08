import numpy as np

a = np.arange(10)
print(a)

print(a.sum())

"""
There can be cases where some of the mathematical functions are not available 
within numpy
"""

# sigmoid 
# f(x) = 1 / (1 + e^(-x))

def sigmoid(array):
    return 1 / (1 + np.exp(-array))
    
print(sigmoid(a))

# Mean squared error 
actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)
print(actual)
print(predicted)

def mse(actual, predicted):
    return np.mean((actual - predicted)**2)

print("MSE \n", mse(actual, predicted))

# binary cross entropy
