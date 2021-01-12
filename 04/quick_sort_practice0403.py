# 리스트에서 가장 큰 수 찾기
def search_largest(arr):
    if len(arr) < 2:
        return arr[0]
    else:
        pivot = arr[0]
        greater = [i for i in arr[1:] if i > pivot]
        return search_largest(greater) if len(greater) != 0 else pivot


print(search_largest([10, 5, 2, 3, 7, 15, 31]))


def solution_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = solution_max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(solution_max([10, 5, 2, 3, 7, 15, 31]))