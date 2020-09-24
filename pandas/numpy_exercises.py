import numpy as np


# 1
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)
array=np.ones(10)
print("An array of 10 ones:")
print(array)
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

# 2
v = np.arange(15,55)
print("Original vector:")
print(v)
print("All values except the first and last of the said vector:")
print(v[1:-1])

# 3
x = np.arange(21)
print("Original vector:")
print(x)
print("After changing the sign of the numbers in the range from 9 to 15:")
x[(x >= 9) & (x <= 15)] *= -1
print(x)

# 4
x = np.array([1, 8, 3, 5])
print("Vector-1")
print(x)
y= np.random.randint(0, 11, 4)
print("Vector-2")
print(y)
result = x * y
result_dot = np.dot(x, y)
print("Multiply the values of two said vectors:")
print(result)

# 5
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)

# 6
x = np.array([[0,1],[2,3]])
print("Original array:")
print(x)
print("Sum of all elements:")
print(np.sum(x))
print("Sum of each column:")
print(np.sum(x, axis=0))
print("Sum of each row:")
print(np.sum(x, axis=1))

# 7
x = np.arange(10)
y = np.arange(11, 20)
print("Original arrays:")
print(x)
print(y)
np.savez('temp_arra.npz', x=x, y=y)
print("Load arrays from the 'temp_arra.npz' file:")
with np.load('temp_arra.npz') as data:
    x2 = data['x']
    y2 = data['y']
    print(x2)
    print(y2)

# 8
a = np.array([1, 2, 3, 4, 5, 6])
print("Original array:")
print(a)
a_bytes = a.tostring()
a2 = np.fromstring(a_bytes, dtype=a.dtype)
print("After loading, content of the text file:")
print(a2)
print(np.array_equal(a, a2))

# 9
a = np.array([[10,40],[30,20]])
print("Original array:")
print(a)
print("Sort the array along the first axis:")
print(np.sort(a, axis=0))
print("Sort the array along the last axis:")
print(np.sort(a))
print("Sort the flattened array:")
print(np.sort(a, axis=None))
