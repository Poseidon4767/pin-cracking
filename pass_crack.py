import random
from time import sleep

characters = "0123456789"
c = 0

# input password
pwd = int(input("Enter pin of 1-5 digits: "))
pwd = str(pwd)
pass_range = len(pwd)
sleep(1)
if pass_range <= 5:
    print("Let's crack your password😉")
    sleep(1)

    password = ""

    while password != pwd:
        password = ""
        for i in range(pass_range):
            password += random.choice(characters)
            print(password)
            print("Cracking password....Please wait")
            #sleep(0.0001)
            c += 1
    print("Successful!!")
    print("Password:", password)
    print("Tries: ", c)
else:
    print("Pin limit is 1-5 digits! Try again.")