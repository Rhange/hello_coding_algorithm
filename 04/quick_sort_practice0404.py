import random

# Binary Search is also divide-and-conquer
def binary_search(arr, answer):
    arr.sort()
    print(arr)
    pivot = arr[len(arr) // 2]
    if pivot > answer:
        next_arr = arr[: (len(arr) // 2)]
    elif pivot < answer:
        next_arr = arr[(len(arr) // 2 + 1) :]
    else:
        return pivot  # base case

    return binary_search(next_arr, answer)  # recursive case


array = [10, 5, 2, 3, 7, 15, 31]

answer = random.choice(array)

print(binary_search(array, answer))