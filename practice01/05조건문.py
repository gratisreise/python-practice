# if문 
age = 20
if age >= 18:
    print("성인입니다.")

# if-else문
age = 15

if age >= 18:
    print("성인")
else:
    print("미성년자")

# if-elif-else문
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 조건식(비교 + 논리)
age = 25

if age > 20 and age < 30:
    print("20대")

#들여쓰기(들여쓰기 = 블록)
if True:
    print("실행됨")
    print("여기도 실행")

# 중첩
age = 20
gender = "남"

if age >= 18:
    if gender == "남":
        print("성인 남성")

# 7. 한 줄 if (삼항 연산자)
age = 20

result = "성인" if age >= 18 else "미성년자"
print(result)

#8. 실전 예제
num = int(input("숫자 입력: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")