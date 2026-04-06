# 집합: 중복을 허용하지 않는 자료구조다.
s = {1, 2, 3}
# 순서 X
# 중복 X
# 수정 O


# 생성
s = {1, 2, 3}

# 빈 set (주의)
s = set()

# 값 추가/ 삭제
s = {1, 2, 3}

s.add(4)        # 추가
s.remove(2)     # 삭제 (없으면 에러)
s.discard(10)   # 삭제 (없어도 OK)

# 포함 여부
s = {1, 2, 3}

print(2 in s)  # True

#중복제거
arr = [1, 2, 2, 3, 3]

s = set(arr)

print(s)  # {1, 2, 3}

# 집합연산
a = {1, 2, 3}
b = {3, 4, 5}

#교집합
a & b        # {3}
a.intersection(b)

#합집합
a | b        # {1,2,3,4,5}
a.union(b)

#차집합
a - b        # {1,2}
a.difference(b)

#반복문
for x in s:
    print(x)