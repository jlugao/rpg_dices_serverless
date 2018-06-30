from random import randrange
from functools import partial

def lanca_dx(val):
    return randrange(1, val + 1, 1)

lanca_d4 = partial(lanca_dx,4)
lanca_d6 = partial(lanca_dx,6)
lanca_d8 = partial(lanca_dx,8)
lanca_d10 = partial(lanca_dx,10)
lanca_d12 = partial(lanca_dx,12)
lanca_d20 = partial(lanca_dx,20)