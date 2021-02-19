# fact 함수에 대한 각각의 호출이 *자기만의 x값의 사본*을 가지고 있다.
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))