# 반환값이란? 👉 함수 실행 결과를 밖으로 돌려주는 것

# def 함수():
#     return 값

# return이 없는 경우
def add(a, b):
    result = a + b

print(add(1, 2))

def add(a, b):
    return a + b

print(add(1, 2))

# return vs print (중요 차이)
def add(a, b):
    print(a + b)

result = add(1, 2)
print(result)

#return 이후 코드
def test():
    print("A")
    return
    print("B")

# 여러 값 반환
def calc(a, b):
    return a + b, a * b

result = calc(2, 3)
print(result)
# ✔ tuple로 반환됨

# 언패킹
sum_val, mul_val = calc(2, 3)
print(sum_val, mul_val)


#조건에 따른 반환
def check(num):
    if num > 0:
        return "양수"
    else:
        return "음수 또는 0"

print(check(10))