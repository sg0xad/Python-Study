# 내장함수

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir()) # import 하기 전
# import random # 외장함수
# print(dir()) # import 한 후
# print(dir(random)) # random 모듈 내에서 쓸 수 있는 것들

# lst = [1, 2, 3]
# print(dir(lst)) # 리스트에서 쓸 수 있는 것들

name = "Jim"
print(dir(name)) # name 변수에 대해서 쓸 수 있는 것들

# 이외에도 구글에 list of python builtins 를 검색해서 내장함수에 대해서 알 수 있다.

