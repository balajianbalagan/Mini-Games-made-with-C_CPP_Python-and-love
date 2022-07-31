import random
import time
ans=random.randint(1,50)
print("\n Hello world!!!!")
time.sleep(2)
print("\n Welcome to random number guessing game")
time.sleep(2)
print("\n Guess a number withing 5 chances")
time.sleep(2)
state=0
for i in range(5):
    print("\n Enter your Guess No.",i+1,': ')
    inp=int(input())
    if(abs(ans-inp)>5 and abs(ans-inp)<=10 and (ans!=inp) and i!=4):
        print("\nYou are close to the answer")
    if(abs(ans-inp)<=5 and (ans!=inp) and i!=4):
        print("\n You are very close to the answer")
    if(abs(ans-inp)>10 and abs(ans-inp)<=20 and (ans!=inp) and i!=4):
        print("\n You are far to the answer")
    if(abs(ans-inp)>20 and (ans!=inp) and i!=4):
        print("\n You are very far to the answer")
    if(ans==inp):
        print("\n YAAY You Win!")
        state=1
        break
if(state==0):
    print("\n SORRY :( You Lose")
    print("\n The answer is: ",ans)