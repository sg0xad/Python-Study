# 오버라이딩# 상속

# 일반 유닛 (부모 클래스)
class Unit:
    def __init__(self, name, hp, speed): # 생성자
        self.name = name  # 멤버 변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

   
# 공격 유닛 (자식 클래스)
class AttackUnit(Unit): # Unit을 상속
     def __init__(self, name, hp, speed, damage): # 생성자
        Unit.__init__(self, name, hp, speed) # 부모 생성자 호출
        self.damage = damage

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중 상속
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location): # 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location) 

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)
vulture.move("11시")

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # Unit 클래스의 move 메소드가 호출되지 않고 FlyableAttackUnit클래스의 move메소드가 호출 (오버라이딩)