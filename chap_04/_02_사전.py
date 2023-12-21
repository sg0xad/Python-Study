# 사전 (dictionary)

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # Error
print(cabinet.get(5)) # None
print(cabinet.get(5, "사용가능")) # 사용가능

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"]
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet) # {}