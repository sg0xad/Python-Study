# continue와 break

absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 9, 10
    if student in absent:  # student 요소가 absent에 포함되어 있다면
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은(는) 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))