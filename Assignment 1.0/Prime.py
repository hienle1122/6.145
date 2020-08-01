import math
def prime (x):
    if x==1 or x==0:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    else:
        return True 

print( prime(4))
