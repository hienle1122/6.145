import math 
def perfect_square(x):
    if x==1 or x==0: 
        return True
    if math.sqrt(x)%1==0:
        return True
    else:
        return False
print( perfect_square(89))
