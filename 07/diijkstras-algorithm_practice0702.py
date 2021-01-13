# graph part
graph = {}

graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30

graph["c"] = {}
graph["c"]["a"] = 1

graph["fin"] = {}

print(graph)

# cost part
costs = {}

infinity = float("inf")
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

print(costs)


# parents part
parents = {}

parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

print(parents)

# processed list
processed = []

# Main

## get lowest_cost_node
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
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