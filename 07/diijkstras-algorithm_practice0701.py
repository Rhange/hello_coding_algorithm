# graph 생성 파트
graph = {}

graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["d"] = 6
graph["c"]["fin"] = 2

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

print(graph)

# costs part
costs = {}

infinity = float("inf")
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# parents part
parents = {}

parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

# 완료 목록

processed = []

# 메인

## 가장 싼 노드 가져오기
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:    # processed에 없어야 한다!
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
   
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    
    processed.append(node)

    print(f"costs => {costs}", f"parents => {parents}", f"processed => {processed}")

    node = find_lowest_cost_node(costs)

# print(f"costs hash table => {costs}")
# print(f"parents hash table => {parents}")