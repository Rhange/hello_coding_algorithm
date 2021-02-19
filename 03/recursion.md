# Recursion Function (재귀 함수)

- 가장 우아한 해결 방법 중의 하나인 재귀(recursion)을 다룬다.

## 기본 단계(base case)와 재귀 단계(recursive case)

- Recursion(재귀)란 함수가 **자기 자신을 호출하는 것**을 말함
- 재귀 함수를 만들 때, 언제 재귀를 멈출지 알려주지 않으면 무한 루프에 빠진다.
- 모든 재귀 함수는 기본 단계(base case)와 재귀 단계(recursive case)라는 두 부분으로 나누어져 있다.
- 기본 단계(base case)에서 재귀를 언제 멈출지 설정할 수 있다.

## 스택(stack)

- push & pop
- Call stack(호출 스택)
- 스택을 사용하면 편리하기는 하지만 모든 정보를 저장해야 하므로 메모리를 많이 소비한다.
- 재귀 대신 반복문을 써서 코드를 다시 작성하거나 tail recursion(꼬리 재귀)를 활용할 수 있다. 꼬리 재귀는 이 책에서 다루지는 않는다.

## 요약

- 재귀는 **함수가 스스로를 호출**하는 것
- 모든 재귀 함수는 '기본 단계(base case)'와 '재귀 단계(recursive case)'라는 두 부분으로 나누어져 있습니다.
- 스택(stack)에는 push와 pop이라는 두 가지 연산이 있다.
- 모든 함수 호출(call)은 call stack을 사용한다.
- Call stack은 너무 커져서 메모리를 엄청나게 소비할 수도 있다.
