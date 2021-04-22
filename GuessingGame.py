import random
r = random.randint(0,9)
print("I have a number from 0 to 9 in my mind.Try Guessing it within five attempts")
attempts = 5
i = 0
s = 1
for i in range(0,5):
    if s==1:
        x = int(input("Enter your guess"))
    if x==r:
        s = 0
        print("You guessed it.")
    elif(x>r):
        attempts = attempts - 1
        print("your guess was high.try again")
        print("You have ", attempts , "remaining")
    elif(x<r):
        attempts = attempts - 1
        print("your guess was low.try again")
        print("You have ", attempts , "remaining")

if attempts==0:
    print("You lose. The number I have in my mind is: ", r)