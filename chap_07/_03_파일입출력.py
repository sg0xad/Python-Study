# 파일입출력

score_file = open("score.txt", "w", encoding="utf8") # w은 쓰기(덮어쓰기) endcoding을 utf8이면 한글 호환
print("수학 : 0", file=score_file) # file=score_file은 표준출력 대신 score_file이라는 파일에 쓰겠다는 의미
print("영어 : 50", file=score_file)
score_file.close() # 파일 닫기

score_file = open("score.txt", "a", encoding="utf8") # a는 append(추가)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # 줄바꿈이 안되므로 \n
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r은 read
print(score_file.read()) # 한번에 모든 내용 불러옴
score_file.close()

print("-----------------------")

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 일고 커서는 다음 줄로 이동 (end=""를 붙이면 커서 이동 x)
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

print("-----------------------")

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: # 값이 없으면
        break
    print(line)
score_file.close()

print("-----------------------")

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line)
score_file.close()