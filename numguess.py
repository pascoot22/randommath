import random

print("Welcome to my number guessing game")
key = str(random.randint(100,999))

won = False
for i in range(7):
    guess = input("enter a three digit guess: ")
    while len(guess) != 3:
        guess = input("no, three digits buddy, try again: ")
    if key == guess:
        print("congrats, you're right")
        won = True
        break
    copy = []
    for c in key:
        copy.append(c)
    digits = 0
    places = 0
    for i in range(3):
        if guess[i] == key[i]:
            places += 1
    for i in range(3):
        if guess[i] in copy:
            digits += 1
            copy.remove(guess[i])
    if digits == 1:
        print(str(digits) + " correct digit, " + str(places) + " placed correctly")
    else:
        print(str(digits) + " correct digits, " + str(places) + " placed correctly")




if not(won):
    print("oof you lost, the number was " + key)




