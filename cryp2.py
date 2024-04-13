import random

def luhn(s):
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
    return ((10 - (count % 10)) % 10)

print("Welcome to my number game, try to find out the code to get in, each guess it will change, try to figure it out")
key = random.randint(10000,99999)
guess = int(input("what is your guess: "))
while True:
    if guess == key:
        break
    print("wrong, the key was " + str(key))
    if key % 2 == 1:
        key += guess
    else:
        key -= guess
    key = key % 10000
    if key < 10000:
        key += 10000
    guess = int(input("try again: "))
print("Congrats, you broke the code") 
again = input("But that code was moderatly simple, do you want to try a new one (y/n): ")
while again == "y":
    key = str(random.randint(100000000000000,999999999999999))
    guess = int(input("what is the last number in this sequence: " + key + " "))
    ans = luhn(key)
    if guess == ans:
        print("Congrats, you solved it, but was that just guesswork")
        break
    print("wrong, try again: ")
    
print("That is all I have today, bye")