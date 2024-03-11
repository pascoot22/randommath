s = input("Enter the first 15 digits: ")

count = 0
a = True
for j in s:
    i = int(j)
    if a:
        a = False
        if i * 2 > 9:
            count += (i * 2) % 10 + int((i * 2) / 10)
        else:
            count += i * 2
    else:
        a = True
        count += i
print((10 - (count % 10)) % 10)