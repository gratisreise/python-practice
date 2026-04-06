#딕셔너리는 key-value(키-값) 형태로 데이터를 저장하는 자료구조다.
d = {"name": "kim", "age": 20}
# 순서 O (파이썬 3.7+)
# 중복 X (key 기준)
# 수정 O

# 생성
d = {}
d = dict()

d = {
    "name": "kim",
    "age": 20
}

# 값 접근
d = {"name": "kim", "age": 20}

print(d["name"])  # kim

d["job"]  # 없는 키 접근 ❌ KeyError
d.get("job")         # None
d.get("job", "없음")  # 없음

# 값 추가/수정 
d = {"name": "kim"}

d["age"] = 20     # 추가
d["name"] = "lee" # 수정

# 삭제
d = {"a": 1, "b": 2}

del d["a"], d.pop("b")

# 반복문 
d = {"a": 1, "b": 2}

for key in d:
    print(key)

for key, value in d.items():
    print(key, value)


# 포함 여부
d = {"a": 1}

print("a" in d)  # True (key 기준)


# 자주 쓰는 메서드
d.keys()    # key 목록
d.values()  # value 목록
d.items()   # (key, value)