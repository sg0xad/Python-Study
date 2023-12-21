# 표준입출력

print("Pyton", "Java", sep=",", end="? ") # sep: 각 값 사이에 넣을 문자열, end: 문장의 끝부분에 넣을 문자열
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():  # items() 메소드는 key와 value
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust는 8개의 크기를 확보하고 왼쪽 정렬, rjust는 4개의 크기를 확보하고 오른쪽 정렬
    # 참고: ljust, rjust 메소드는 문자열에 대해서만 동작하므로 str(score)으로 자료형 변환을 해야 함.

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3)) # 3개의 공간을 확보하고 빈공간은 0으로 채움

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
print(type(answer)) # input으로 사용자 입력을 받을 때는 항상 문자열로 저장
