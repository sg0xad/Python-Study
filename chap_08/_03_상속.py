# 상속

# 일반 유닛 (부모 클래스)
class Unit:
    def __init__(self, name, hp): # 생성자
        self.name = name  # 멤버 변수
        self.hp = hp
   
# 공격 유닛 (자식 클래스)
class AttackUnit(Unit): # Unit을 상속
     def __init__(self, name, hp, damage): # 생성자
        Unit.__init__(self, name, hp) # 부모 생성자 호출
        self.damage = damage
      
     def attack(self, location): # self는 자기자신을 의미하며 메소드에는 항상 self 필요
         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp -= damage
         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
         if self.hp <= 0:
             print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향을 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) 
valkyrie.fly(valkyrie.name, "3시")
valkyrie.attack("3시")
            