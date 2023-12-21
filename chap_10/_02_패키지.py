# 패키지

import travel.thailand # 모듈이나 패키지만 가능하다. 즉, 클래스나 함수는 import를 할 수 없다.
trip_to = travel.thailand.ThailangPackage()
trip_to.detail()

from travel.thailand import ThailandPackage # from import 에서는 모듈, 패키지, 클래스, 함수 모두 가능
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()