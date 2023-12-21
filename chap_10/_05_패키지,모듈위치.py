# 패키지, 모듈 위치

import inspect
import random
print(inspect.getfile(random)) # random 모듈이 어느 위치에 있는지

from travel import *
print(inspect.getfile(vietnam))