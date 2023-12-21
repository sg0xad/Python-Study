# 클래스

class Unit:
    def __init__(self, name, hp, damage): # 생성자
        self.name = name  # 멤버 변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.name, self.damage))

marine1 = Unit("마린", 40, 5) # marine1 같은 변수를 객체라고 하고 Unit 클래스의 인스턴스라고도 한다. 
tank1 = Unit("탱크", 150, 35)
tank2 = Unit("탱크", 150, 35)
# marine3= Unit("유닛", 40) # self를 제외한 동일한 개수의 인수를 전달해야 함

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (뺴앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 멤버 변수를 외부에서 할당 (다른 객체는 적용 x)

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))