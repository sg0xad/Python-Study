# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 모두 소문자로
print(python.upper()) # 모두 대문자로
print(python[0].isupper()) # 0번째가 대문자인지 확인 (true)
print(len(python)) # 문자열 길이 반환 (17)
print(python.replace("Python", "Java")) # Python 문자를 Java로 변환

index = python.index("n")
print(index) # 5
index = python.index("n", index + 1) # 15 (두번째 n)

print(python.find("Java")) # -1
# print(python.index("Java")) Error

print(python.count("n")) # python 변수에서 n이 총 몇개 있는지 (2)

