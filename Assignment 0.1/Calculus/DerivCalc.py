poly = [0, 0, 1/2]
l=len(poly)-1
i=0
x=[]
value=0
while i <= l :
     value = poly[i] * i
     if i > 0:
         x.append(value)
     i=i+1
print(x) 
