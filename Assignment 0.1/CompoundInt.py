interest_rate = .01
a=0
p=1
t=0
if interest_rate==0:
    print("NEVER")

if interest_rate > 0:   
    while a < 2*p:
        a = p * ( 1 + interest_rate ) ** t
        t = t+1
    print(t-1)
