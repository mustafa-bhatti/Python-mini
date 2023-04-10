##Guess Game
import random
num=random.randint(1,50)
flag=False 
i=1
while (flag == False and i <=6):
   n=int(input("Guess the number : "))
   if n == num:
       flag= True
       print ("Congratulations!!!" )
   elif n < num:
       print ("Guess is low")
   elif n > num:
       print ("Guess is high")
   i=i + 1
if flag == False:
    print (f"Correct Number : {num} \n try again")
