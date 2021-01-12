# 리스트에 포함된 원소의 숫자를 세는 재귀 함수
def echo(arr):
    if len(arr) == 1:
        print(arr[0])
    else:
        print(arr[0])
        return echo(arr[1:])


# echo([1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15])


def solution_count(list):
    if list == []:
        return 0
    return 1 + solution_count(list[1:])


print(solution_count([1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 15]))