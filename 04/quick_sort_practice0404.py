import random

# Binary Search is also divide-and-conquer
def binary_search(arr, answer):
    pivot = arr[0]
    if pivot > answer:
        next_arr = [i for i in arr[1:] if i < pivot]
    elif pivot < answer:
        next_arr = [i for i in arr[1:] if i > pivot]
    else:
        return pivot    # base case
    
    return binary_search(next_arr, answer)  # recursive case

array = [10, 5, 2, 3, 7, 15, 31]

answer = random.choice(array)

print(binary_search(array, answer))