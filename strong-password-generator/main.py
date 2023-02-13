import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

characters_number = input("How many characters for the password? ")
while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("You need at least 6 characters!")
            characters_number = input("Please the number again ")
        else:
            break
    except:
        print("Please enter numbers!")
        characters_number = input("How many characters for the password? ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

percentage1 = round(characters_number * (30/100))
percentage2 = round(characters_number * (20/100))

password = []

for i in range(percentage1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(percentage2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[:characters_number])

print(password)