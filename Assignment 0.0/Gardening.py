sideLength = 61
plantSpace = .3
soilDep = 5
gravelDep = 3
totArea = sideLength ** 2
gravelArea = ((sideLength / 4)**2 * 3.1415926)*3
plantArea = totArea-gravelArea
gravelTot = (gravelArea * gravelDep) / 27
soilTot = (plantArea * soilDep)/ 27
smallBedArea =  (sideLength / 2) ** 2 - ((sideLength / 4)**2 * 3.1415926)
largeBedArea = totArea - ((sideLength / 2) **2) - ((sideLength / 4)**2 * 3.1415926)*2
print ("Plants per large flower bed")
print ( (largeBedArea / 4) // plantSpace ** 2)
print ("Plants per small flower bed")
print ( (smallBedArea / 4) // plantSpace ** 2)
print ('Soil for each large flower bed' ) 
print( (largeBedArea / 4 * soilDep)/27 )
print ('Soil for each small flower bed' ) 
print( (smallBedArea / 4 * soilDep)/27 )
print( 'Total Volume of Soil')
print(soilTot) 
print( 'Total Volume of Gravel')
print(gravelTot)




