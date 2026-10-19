#guess the number game 
import random
target=random.randint(1,10)

while True:
    userchoice=input("guess the target or quit:")
    if userchoice=="quit":
        break
    userchoice=int(userchoice)
    if (userchoice==target):
        print("YAYY! CORRECT GUESS")
        break
    elif(userchoice>target):
        print("oopss go lower!")
    else:
        print("oopss go higher!")
print("-----GAME OVER-----")
