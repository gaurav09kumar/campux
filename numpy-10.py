import numpy as np
import matplotlib.pyplot as plt

# Working with missing values

a = np.array([1,2,3,4,np.nan,6])
print(a)
# When we speak about nan it means empty values

# Remove the missing values
print(a[~np.isnan(a)])

# Plotting graphs - we can plot any mathematical function graph
# x = y

x = np.linspace(-10, 10, 100)
print(x)
y = x

# x = y
plt.plot(x, y)

# x = y**2
plt.plot(x , x**2)

# y = sin(x)
plt.plot(x, np.sin(x))

# y = x * log(x)
plt.plot(x, x * np.log(x))


# sigmoid graph
x = np.linspace(-10,10,100)
y = 1/(1+np.exp(-x))
plt.plot(y)
