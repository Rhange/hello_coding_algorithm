voted = {}

# get 함수는 해시 테이블 안에 "tom"이라는 key가 있으면
# 그 key에 해당하는 value를 반환한다.
# 만약 없다면, None을 반환한다.
value = voted.get("tom")

def check_voter(name):
    if voted.get(name):
        print("쫓아내세요!")
    else:
        voted[name] = True
        print("투표하게 하세요.")


check_voter("tom")
check_voter("mike")
check_voter("mike")