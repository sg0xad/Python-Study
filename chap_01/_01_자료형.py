# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
print("-------------------------------")

# 문자열 자료형
print('풍선')
print("나비")
print("aaaa")
print("a" * 4) # aaaa
print("-------------------------------")

# boolean(참 / 거짓) 자료형
print(5 > 10) # False
print(5 < 10) # True
print(True)
print(False)
print(not True)     # False
print(not False)    # True
print(not (5 > 10)) # True
print("-------------------------------")

# 변수
animal = "강아지"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이예요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") # 콤마로 연결 할 때는 자료형변환을 안해도 된다.
print("연탄이는 어른일까요? " + str(is_adult))
print("-------------------------------")

# 주석
# 주석을 편하게 하고 싶으면 드래그 한 뒤 Ctrl + /
''' 이렇게
하면
여러문장이
주석처리
됩니다. '''