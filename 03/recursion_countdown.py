# 무한 루프에 빠지는 예시 코드
# def countdown(i):
#     print(i)
#     countdown(i - 1)

# 무한 루프에 빠지지 않는 코드
def countdown(i):
    print(i)
    if i <= 1:  # base case
        return
    else:
        countdown(i - 1)    # recursive case

countdown(10)