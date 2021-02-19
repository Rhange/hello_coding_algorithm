# 가장 작은 수의 인덱스 return
def findSmallest(arr):
    smallest = arr[0]  # 가장 작은 정수를 저장
    smallest_index = 0  # 가장 작은 정수의 인덱스를 저장

    for i in range(1, len(arr)):  # 처음 인덱스 이후의 값들을 loop
        if arr[i] < smallest:  # 해당 인덱스 위치의 값이 더 작다면
            smallest = arr[i]  # 가장 작은 정수 새로 할당
            smallest_index = i  # 가장 작은 정수의 인덱스 값을 새로 할당
    return smallest_index  # 인덱스 값만 리턴


# 가장 작은 수의 인덱스로부터 해당 수를 꺼내고
# arr에서 삭제한 뒤, 새로운 array에 순서대로 삽입
def selectionSort(arr):
    newArr = []  # 정렬된 배열을 만들기 위해 빈 배열 초기화

    for i in range(len(arr)):  # 배열의 갯수만큼 루프
        smallest = findSmallest(arr)  # 가장 작은 원소의 인덱스 얻기
        newArr.append(arr.pop(smallest))  # 해당 인덱스 위치의 원소 제거 및 새로운 배열에 추가
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))  # [2, 3, 5, 6, 10]