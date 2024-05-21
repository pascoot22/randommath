import random
import time
 
# while True:
#     a = input("Give a five digit num: ")
#     while int(a) < 10000 or int(a) > 99999:
#         a = input("no, a five digit number: ")
#     key = random.randint(10000,99999)
#     print(key)
#     num = 0
#     for i in range(0,5):
#         sk = str(key)

#         j = (int(sk[i]) + int(a[i])) % 10
#         num += j * 10 ** (4-i)
#         print(num)

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
        






        

        
    


