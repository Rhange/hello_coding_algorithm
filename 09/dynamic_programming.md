# Dynamic Programming

- 어려운 문제를 여러 개의 하위 문제로 쪼개고, 이 하위 문제들을 먼저 해결하는 방법인 동적 프로그래밍 기법을 학습
- 예제를 사용하여 동적 프로그래밍을 새로운 문제에 어떻게 적용하는지 학습

## 배낭 채우기 문제(knapsack problem)

- 4파운드(lbs)의 짐을 넣을 수 있는 배낭
- 훔칠 수 있는 물건
  - 스테레오 ($3000, 4 lbs)
  - 노트북 ($2000, 3 lbs)
  - 기타 ($1500, 1 lb)

1. 단순한 방법

   - 모든 물건의 조합을 시도해서 각 경우의 총 가치를 모두 구해본다.
   - 가장 가치가 높은 경우를 선택한다.
   - 알고리즘의 실행 시간, O(2<sup>n</sup>)
   - 너무 느리다.

2. 동적 프로그래밍

   - 하위 배낭(sub-knapsack)에 대한 문제를 풀고 이를 이용해서 원래의 문제를 푼다.
   - 모든 동적 프로그래밍 알고리즘은 **격자(grid)**로부터 시작한다.
   - 동적 프로그래밍은 각 하위 문제들이 서로 관계가 없을 때, 즉 서로 **의존하지 않는 경우**에만 쓸 수 있다.

   1. 자주하는 질문

      1. 만약 물건이 추가된다면? 새로운 행이 추가 된다.
      2. 행의 순서가 바뀐다면? 문제없다.
      3. 열 방향으로 채워도 되는가? 예제에서는 차이가 없지만 다른 문제에서는 달라질 수도 있다.
      4. 더 작은 물건을 추가한다면? 격자를 가장 작은 물건에 맞게 세분화해야 한다.
      5. 물건의 일부만 훔칠 수도 있는가? No. 동적 프로그래밍으로 풀 수 있는 것은 물건 하나를 통으로 훔치던가, 아예 훔치지 않는가 하는 문제뿐이다. 물건을 반으로 나눈다거나 하는 경우는 풀 수 없다. 이 경우는 탐욕 알고리즘으로 쉽게 풀 수 있다.
      6. 하위 배낭이 두 개 이상인 경우도 있는가? No. 최대 두개의 배낭을 합칠 수 있다. 하지만 그 배낭 중의 하나가 두 개의 더 작은 배낭으로 이루어져 있을 수는 있다.
      7. 배낭을 완전히 채우지 못하는 경우도 있는가? Yes. 하나의 물품이 말도 안되게 비싼 경우. 그 물품 하나만이 공간을 차지하고 공간이 남아 있을 수 있다.

   2. 비슷한 예제
      1. 여행 일정 최적화 문제

## 중간 정리

- 동적 프로그래밍은 **어떤 제한 조건이 주어졌을 때** **무언가를 최적화**하는 경우에 유용하다.
- 배낭 채우기 문제에서는 **배낭의 크기가 제한 조건**이었고, 이때 **훔칠 물건의 총 가치를 최대화**하는 것이 목표였다.
- 동적 프로그래밍은 하위 문제가 **서로 의존하지 않는 경우**에만 사용할 수 있다.

- 모든 동적 프로그래밍의 답안에는 **격자(grid)**가 있다.
- 격자의 각 칸에는 최적화하고자 하는 값을 적는다.
- 배낭 문제의 경우에는 모든 물건의 총 가치를 썼다.
- 각 칸은 원래 문제에 대한 하위 문제이고, 다른 문제를 하위 문제로 가질 수 있다.
- 그러므로 원래의 문제를 어떻게 하위 문제로 나눌 수 있을지 생각해야 한다.
- 그러면 각각의 축이 어떻게 되어야 하는지 알아내는 데 도움이 된다.

- 동적 프로그래밍에서는 **무언가를 최대화**하는 것이 목표이다.

## 또 다른 예시: 최장 공통 부분 문자열(LCS, Longest Common Substring)

- 배낭 채우기 문제와는 달리 마지막 칸의 숫자가 답이 아닐 수 있다.
- 이 문제에서 답은 격자 전체에서 가장 큰 숫자이다.

## 최장 공통 부분열(Longest Common Subsequence)

- 글자가 다른 경우에 부분 문자열에서 '0'을 입력하는 것과 달리 왼쪽 또는 위쪽 칸 중에서 더 큰 값을 가져온다.

## 파인만 알고리즘(Feynman Algorithm)

1. 문제를 작성한다.
2. 열심히 생각한다.
3. 답을 쓴다.

## 동적 프로그래밍이 현실에서 정말 쓰이는가?

1. 생물학자는 DNA 가닥의 유사점을 찾기 위해 최장 공통 부분열 방법을 사용한다. 그러면 두 종류의 동물이나 질병이 얼마나 비슷한지 알 수 있다. 최장 공통 부분열 방법은 다바성 경화증이라는 병의 치료법을 찾는 데도 쓰인다.

2. git diff와 같은 diff 명령을 써 본적이 있는가? diff 명령은 두 파일의 차이점을 찾아준다. 그리고 그렇게 하기 위해 동적 프로그래밍을 사용한다.

3. 우리는 문자열의 유사성을 따지고 있다. 레벤슈타인의 거리(Levenshtein distance)는 두 문자열의 유사성을 측정한다. 물론 동적 프로그래밍을 사용한다. 레벤슈타인의 거리는 철자법 확인이나 누군가의 지적 재산권이 있는 데이터를 인터넷에 업로드했는지 확인하는 데도 쓰인다.

4. MS word와 같은 프로그램에서 줄 맞추기 기능을 사용해 본적이 있는가? 줄의 길이를 일관성 있게 맞추기 위해 어떻게 할까? 바로 동적 프로그래밍을 사용한다!

## 정리

- 동적 프로그래밍은 **제한 조건**이 있는 경우에 무언가를 **최적화**할 때 유용하다.
- 동적 프로그래밍은 큰 문제를 작은 하위 문제로 나누어 푸는 방법이다.
- 동적 프로그래밍을 풀 때는 **격자(grid)**를 사용한다.
- 보통 격자의 각 칸에는 **최적화하려는 값**을 쓴다.
- **격자의 각 칸은 하위 문제를 뜻한다.** 그러므로 원래의 문제를 어떻게 하위 문제로 나눌 수 있는지 생각해야 한다.
- 동적 프로그래밍의 해답을 계산해 주는 쉬운 공식 같은 것은 없다.
