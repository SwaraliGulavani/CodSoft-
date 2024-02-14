import random
def check(comp,user):
    if comp ==user:
        return 0
    
    if(comp == 0 and user ==1):
      return 1
    if (comp == 1 and user ==2):
       return 1 
    if(comp == 2 and user ==0):
       return 1
    
    return -1
while True:
   try:
      comp = random.randint(0,2)
      user = int(input("0 for Rock, 1 for Paper and 2 for Scissor:"))
      
         
      print("You :",user)
      print("Computer:", comp)
      score = check(comp,user)
      if(score== 0):
         print(" Its a draw")
      elif(score == 1):
         print("You Won")
      else:
         print("You Lose")

   except ValueError:
      print("Invalid input. Please enter number from 0 to 2 ")
   



     



