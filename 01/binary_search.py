def binary_search(list, item):
    low = 0  # 최소값 인덱스
    high = len(list) - 1  # 최대값 인덱스

    while low <= high:
        mid = (low + high) // 2  # 중간 인덱스, 중간부터 시작
        guess = list[mid]  # 중간 인덱스의 원소값 확인

        if guess == item:  # 추측한 값이 목표값과 같다면
            return mid  # 해당 인덱스 값을 리턴
        if guess > item:  # 추측한 값이 목표값보다 크다면
            high = mid - 1  # 최대값을 중간값보다 작게 설정
        else:
            low = mid + 1  # 추측한 값이 목표보다 작다면 최소값을 중간값 + 1로 설정
    return None  # 찾으려는 값이 list 안에 없다면 None을 리턴


# Test
my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # 3이 있는 인덱스 값을 리턴, 1
print(binary_search(my_list, -1))  # -1은 my_list 안에 없으므로 None을 리턴