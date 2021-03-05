from collections import deque

graph = dict()
graph["you"] = [["alice", 0], ["bob", 0], ["claire", 0]]
graph["bob"] = [["anuj", 1], ["peggy", 0]]
graph["alice"] = [["peggy", 0]]
graph["claire"] = [["tom", 0], ["jonny", 0]]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []


def person_is_seller(mango):
    # 사람 이름이 'm'으로 끝나면 망고 판매상이라고 가정
    return mango == 1


def find_seller(name):
    search_queue = deque()  # 양방향 queue, 현재는 빈 리스트
    search_queue += graph[name]  # deque에 name이 가지고 있는 리스트를 추가
    searched = []

    while search_queue:  # deque에 아무것도 없을때까지 루프 실행
        # 맨 처음(리스트 가장 왼쪽)에 있는 것부터 하나씩 꺼낸다.
        [person, mango] = search_queue.popleft()
        # searched list에 없는 이름이라면
        if not person in searched:
            # 일단 판매상인지 확인한다.
            if person_is_seller(mango):
                # 맞으면 망고 판매상이라는 문자열을 출력하고
                print(f"{person} is a mango seller!")
                # True 리턴
                return True
            # 판매상이 아니라면
            else:
                # 그 사람의 친구 목록을 dequeue에 추가하고
                search_queue += graph[person]
                # 중복을 피하기 위해 그 사람의 이름을 searched 리스트에 추가한다.
                searched.append([person, mango])

    return False


find_seller("you")