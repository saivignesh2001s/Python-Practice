print("Guess random number")
import random
k1=True
while k1:
    i=input("Enter a number")
    try:
        if(i.lower()=="exit"):
            k1=False
            break
        k=int(i)
        j=random.randint(1,10)
        print(j)
        if(k==j):
            print("you guessed the number right")
        else:
            print("Your guess is wrong")
    except:
        print("You entered an invalid number")
print("You exited the loop successfully")

