from collections import deque

graph = {}
graph["CAB"] = ["CAT", "CAR"]
graph["CAT"] = ["MAT", "BAT", "CAR"]
graph["CAR"] = ["CAT", "BAR"]
graph["MAT"] = ["BAT"]
graph["BAR"] = ["BAT"]

def search(start):
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        position = search_queue.popleft()

        if not position in searched:
            if position == "BAT":
                return True
            else:
                search_queue += graph[position]
                searched.append(position)
    
    return False

print(search("CAB"))