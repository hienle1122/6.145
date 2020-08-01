size = 'small'
toppings = ['bacon', 'anchovies','bacon', 'anchovies' ]
price=0
topper=0
addon=False
if size=='small':
    price= 14

if size=='medium':

    price= 16

if size=='large':
    price= 18

for i in range(len(toppings)):
    topper = 12+i+len(toppings[i]) 
    price = price + price * topper / 100
   
for i in range(len(toppings)):
    if toppings[i]=='bacon' or toppings[i]=='anchovies':
        addon=True 
       
if addon==True:
    price= price*1.1
print (price)
