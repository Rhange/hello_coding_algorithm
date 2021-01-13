graph = {}  # 메인 해시 테이블 생성

graph["start"] = {} # 또 다른 해시 테이블 생성
graph["start"]["a"] = 6
graph["start"]["b"] = 2

print(graph["start"].keys())
print(graph["start"]["a"])  # a node로 가는 edge의 weight
print(graph["start"]["b"])  # b node로 가는 edge의 weight

# 그래프에 있는 나머지 node들과 그 neighbor들도 추가
graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}   # 도착점은 neighbor가 없다.


"""
각 node의 가격을 저장하는 해시 테이블
"""

# 가격을 모르는 node는 가격을 무한대로 둔다.

infinity = float("inf")

# 가격에 대한 해시 테이블

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

"""
부모를 나타내는 해시 테이블
"""

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


# 마지막으로 각 정점은 한 번씩만 처리해야 하므로
# 이미 처리한 정점을 추적하기 위한 배열 생성

processed = []


"""
메인 코드
"""

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

node = find_lowest_cost_node(costs) # 아직 처리하지 않은 가장 싼 정점을 찾는다.
while node is not None: # 모든 정점을 처리하면 반복문 종료
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)