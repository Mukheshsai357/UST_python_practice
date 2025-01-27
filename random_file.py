import random
while(True):
    n=int(input("select a number between 1 to 10\n"))
    r=random.randint(1,10)
    if(n==r):
        print("Your guessed correct")
        break
    else:
        print("Sorry,the lucky number is",r,"and your selected number is",n)
        print("So,please select a number between 1 to 10")
