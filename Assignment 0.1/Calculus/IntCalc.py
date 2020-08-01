poly = [3, 4, 5]
const=3
l=len(poly)-1
i=0
x=[const]
value=0
while i <= l :
    value = (poly[i])/(i+1)
    x.append(value)
    i=i+1
print(x) 
