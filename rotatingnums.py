import random
import time

key = random.randint(1000000000000,9999999999999)
a = 0
for i in range(13):
    for j in range(10):
        time.sleep(.04)
        print(a)
        if str(j) == str(key)[i]:
            break
        a += 10**(12-i)

print(key)
        






        

        
    


