def ndoors(ans):
    totdoors=[]
    for i in range(ans):
        i=i+1
        totdoors.append(i)

    counter=[]
    for j in range(ans):
        count=0 
        for m in range (ans) :
            m=m+1
            if totdoors[j] % m == 0: 
                count=count+1
            m=m+1
        counter.append(count)
    list1=[]
    for t in range(len(counter)):
        if counter[t] % 2 != 0 :
            list1.append(t+1)
    return list1
print(ndoors(1000))
        
    

            
        
        
    
        

        
    
 
