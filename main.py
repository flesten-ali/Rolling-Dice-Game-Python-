import random

choice  = input("Press y to play rolling dice : ")

while choice =='y':

     iteration = 0
     userCount = 0
     copmuterCount = 0
     draw = 0

     while iteration < 5:

         userChoice = random.randrange(1,7)
         computerChoice = random.randrange(1,7)
         if userChoice > computerChoice:
             print("user wins!" , userChoice, "vs" , computerChoice)
             userCount +=1 ;
         elif computerChoice > userChoice:
             print("computer wins!", computerChoice, "vs", userChoice)
             copmuterCount += 1;
         else:
             print("Draw no winner!", computerChoice, "vs", userChoice)
             draw+=1
         iteration+=1


     print()
     print("Reporting the result:")
     print("total number of dice roll:" , iteration,"times")
     print("the user won:" ,userCount,"times")
     print("the computer won:" , copmuterCount,"times")
     print("the draws were:",draw,"times")
     print()
     choice  = input("Press y to play rolling dice : ")
     if choice !='y':
       break


if choice!= 'y':
  print("the game has ended")
