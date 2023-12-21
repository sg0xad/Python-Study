# 패스

class Unit:
    def __init__(self, name, hp, location): # 생성자
        self.name = name 
        self.hp = hp
        self.location = location
    def info(self):
        print("건물 정보 : 이름은 {0} 체력은 {1} 위치는 {2} 입니다.".format(self.name, self.hp, self.location))


class BuildingUnit(Unit):
    def __init__ (self, name, hp, location):
        # Unit.__init__(self, name, hp)
        super().__init__(name, hp, location) # 부모 클래스 생성자 호출 (self 정보는 안보내야 함)
     
    def info(self):
        super().info() # 부모 클래스 메소드 호출

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
supply_depot.info()

# -------------------------------------------------------------------------------------

class A:
    def __init__(self):
        print("A 생성자")

class B:
    def __init__(self):
        print("B 생성자")

class C(A, B):
    def __init__(self):
    # super().__init__() # A 클래스 생성자만 호출

    # 두 클래스의 생성자 둘다 호출할려면
        A.__init__(self)
        B.__init__(self)

c = C()
    