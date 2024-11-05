import random
num = random.randint(1,10)
guess = int(input("enter a guesing number 1 to 10:"))
while guess != num:
    if guess<num:
        print("your guesing number is too low")
    elif guess >num:
        print("your guesing number is too high")
    guess = int(input("guess again:"))
print("your guesed number is right...wow...")

