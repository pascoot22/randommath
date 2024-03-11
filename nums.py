n = 1
count = 0
while count < 2023:
    for i in range(n):
        count += n * i
    n += 1
print(n - 1)