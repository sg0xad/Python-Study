# __all__

from travel import * # *로 설정해도 vietnam 같은 특정 모듈을 사용할 수 없다. (사용하려면 패키지 안의 __init__.py에 __all__ 설정)
trip_to = vietnam.VietnamPackage()
trip_to.detail()
# trip2_to = thailand.ThailangPackage() # __init__.py 파일의 __all__ 리스트에 thailand가 없으므로 에러