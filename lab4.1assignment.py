import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)


arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)
zeros = np.zeros(5)
print("Zeros:", zeros)

range_arr = np.arange(0, 10, 2)
print("Range Array:", range_arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))