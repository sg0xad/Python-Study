def profile1(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " => print문이 끝날 때 줄바꿈 하지 않고 공백으로
    print(lang1, lang2, lang3, lang4, lang5)

profile1("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile1("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile2(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()

profile2("강백호", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
profile2("김태호", 25, "Kotlin", "Swift")