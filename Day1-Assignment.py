import numpy as np

"""Question1: Create an array of integers between -10 and 10"""

arr = np.array(range(-10, 11))
print(arr)

"""Question2:  Run the following code to create a NumPy array D"""

D = np.array(range(18)) + 3
print(D)

  """(a) Extract every other value from array D starting from the 2nd value through the 10th value. Store the result in a variable called x."""

X = D[2:11]
print(X)

 """ Extract every other value from array D starting from the 10th value through the 2nd value. Store the result in a variable called y."""

Y = D[2:-7]
print(Y)

  """Create a variable z that contains all of the values in D in reverse order."""
Z = D[::-1]
print(Z)

# Question3: How are NumPy Arrays better than Lists in Python? 
"""
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called the locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also, it is optimized to work with the latest CPU architectures.


"""
