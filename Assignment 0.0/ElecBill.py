kwh_used = 3793
bill=0
if kwh_used <=500:
    bill = kwh_used * .53
if kwh_used >500 and kwh_used <= 1500:
    bill = 500 * .53 + (kwh_used - 500)*.79
if kwh_used > 1500 and kwh_used <=2500:
    bill = 500 * .53 + 1000*.79 + (kwh_used-1500)*1.12
if kwh_used > 2500:
    bill = 500 * .53 + 1000*.79 + 1000*1.12 + (kwh_used - 2500) * 1.7
print (bill*1.2)
