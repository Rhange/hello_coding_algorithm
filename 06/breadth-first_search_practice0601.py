from collections import deque

graph = {}
graph["S"] = ["A", "C"]
graph["A"] = ["B", "F"]
graph["B"] = []
graph["C"] = ["B", "D"]
graph["D"] = ["F"]

def search(start):
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        position = search_queue.popleft()
        if not position in searched:
            if position == "F":
                return True
            else:
                search_queue += graph[position]
                searched.append(position)

    return False


print(search("S"))