# pickle

import pickle
profile_file = open("profile.pickle", "wb") # b는 binary (피클을 사용할 때는 필수), 피클에서는 인코딩 필요 x
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close() 

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
