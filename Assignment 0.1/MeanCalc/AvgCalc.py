numbers = [1,2,3,4]
tot=0
if len(numbers)==0:
    print("None")

for i in numbers:
    tot=tot+i

if len(numbers)!=0:
    print(tot/len(numbers))
