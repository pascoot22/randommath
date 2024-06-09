import random

print("Welcome to my number guessing bot, pick a number a three digit number and I will try to guess it (ie between 000 and 999)")
key = str(random.randint(100,999))

notpossible = [set(),set(),set()]
known = [-1] * 3
found = 0
guess = "123"
zero = False
repeats = False
for i in range(7):
    
    spots = int(input("what are the number of correct spots in " + guess + ": "))
    if spots == 3:
        print("knew it")
        break
    nums = int(input("what are the number of correct numbers in " + guess + ": "))
    found += nums
    if nums == 0:
        for c in guess:
            for s in notpossible:
                s.add(c)
    if spots == 0:
        for i in range(3):
            notpossible[i].add(guess[i])
    print(notpossible)
    

    if found < 3:
        if guess == "123":
            guess = "456"
        elif guess == "456":
            guess = "789"
        elif guess == "789":
            zero = True
        else:
            repeats = True
    
