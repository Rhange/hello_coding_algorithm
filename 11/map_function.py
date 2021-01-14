from functools import reduce

# Map function
arr1 = [1, 2, 3, 4, 5]
arr2 = map(lambda x: 2 * x, arr1)
print(list(arr2))

# Reduce function
arr3 = reduce(lambda x,y: x+y, arr1)
print(arr3)

