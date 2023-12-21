def profile(name, age, main_lang):
    print(name, age, main_lang)

# 순서가 뒤섞여 있어도 키워드=값으로 인수를 전달 가능
profile(name="유재석", main_lang="파이썬", age=20) # 유재석 20 파이썬
profile(main_lang="자바", age=25, name="김태호") # 김태호 25 자바