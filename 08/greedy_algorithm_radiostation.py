states_needed = set(["mt","wa","or","id","nv","ut","ca","az"])

# set(집합) 타입은 각 원소가 한 번씩만 나타난다. 
# 즉, 중복된 원소를 가지지 않는다.

"""
example

arr = [1, 2, 2, 3, 3, 3]
set_arr = set(arr)
print(set_arr)  # set([1, 2, 3])
"""

# 선택된 방송국의 목록 설정 (해시 테이블)

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

## key는 방송국 이름, value는 방송국의 방송을 들을 수 있는 주(states)의 목록

# 방문할 방송국의 목록 집합

final_stations = set()

# 계산하기

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    
    states_needed -= states_covered
    final_stations.add(best_station)

print("final stations: ", final_stations)