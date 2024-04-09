lets = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
rev = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

while True:
    a = input("Do you want to enrypt (0) or decrypt (1), or neither ")
    if a == '0':
        s = input("Enter a string to enrypt: ")
        b = input("Enter a padding: ")
        str = ''
        for i in range(len(s)):
            j = (lets[s[i]] + lets[b[i % len(b)]]) % 26
            str += rev[j]
        print(str)

    elif a == '1':
        s = input("Enter a string to decrypt: ")
        b = input("Enter a padding: ")
        str = ''
        for i in range(len(s)):
            j = (lets[s[i]] - lets[b[i % len(b)]]) % 26
            str += rev[j]
        print(str)
    else:
        break

print("bye")





