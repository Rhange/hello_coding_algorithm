states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# set(집합) 타입은 각 원소가 한 번씩만 나타난다.
# 즉, 중복된 원소를 가지지 않는다.

# example
arr = [1, 2, 2, 3, 3, 3]
set_arr = set(arr)
print(set_arr)  # set([1, 2, 3])

# 선택된 방송국의 목록 설정 (해시 테이블)
## key는 방송국 이름, value는 방송국의 방송을 들을 수 있는 주(states)의 목록
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 최종 방문할 방송국의 목록 집합
final_stations = set()

# 계산하기
while states_needed:
    best_station = None  # 방송 가능한 가장 많은 주를 포함하는 방송국
    states_covered = set()  # 위의 방송국의 주들 목록
    for station, states in stations.items():  # dict.items()는 key, value 내놓는다.
        covered = states_needed & states  # & 는 교집합을 의미, |는 합집합, -는 차집합
        if len(covered) > len(states_covered):  # 해당 방송국이 커버하는 주 갯수가 현재 커버하는 주 갯수보다 많으면 채택
            best_station = station  # 방송국 이름 갱신
            states_covered = covered  # 주 목록 갱신

    states_needed -= states_covered  # 전체 주 목록 갱신
    final_stations.add(best_station)  # 최종 답안 집합에 현재 방송국 추가

print("final stations: ", final_stations)