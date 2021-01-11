# 가장 작은 수의 인덱스 return
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 가장 작은 수의 인덱스로부터 해당 수를 꺼내고
# arr에서 삭제한 뒤, 새로운 array에 순서대로 삽입
def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))