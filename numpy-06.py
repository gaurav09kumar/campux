"""
Numpy came in picture because the python data types were slow

"""

# Numpy array vs python lists
"""
1. Speed
2. Memory occcupied in RAM
3. Convenience
"""

import time
import numpy as np

# Python lists addition
a_list = [i for i in range(10000000)]
b_list = [i for i in range(10000000, 20000000)]

start = time.time()
c_list = []
for i in range(len(a_list)):
    c_list.append(a_list[i] + b_list[i])
print("Time taken with Python lists:", time.time() - start)

# NumPy array addition
a_np = np.arange(10000000)
b_np = np.arange(10000000, 20000000)

start = time.time()
c_np = a_np + b_np  # Vectorized operation
print("Time taken with NumPy arrays:", time.time() - start)
