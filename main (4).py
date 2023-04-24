title='Snake Water Gun'.center(50,'=')
print(title)
import random
score=0
def play_game():
  global score
  user_choice=input("\nEnter s for Snake\nEnter w for Water\nEnter g for Gun\nEnter any Invalid key for Exit! \nEnter Your Response Here: ")
  if user_choice not in ['s','w','g']:
    print("\nInvalid Key Entered!\nExiting Game...")
    return False

  comp_choice=random.choice(['s','w','g'])
  print("\nYou Choose:",user_choice)
  print("Computer Choose:",comp_choice)
  if user_choice==comp_choice:
    print("\nIt's a Tie\nTry Again")
#=================for Snake===============
  elif user_choice=='s':
    if comp_choice=='w':
      print("\nCongratulations!\nYou Won")
      score+=1
    elif comp_choice=='g':
      print("\nHard Luck!\nTry Again")
      score-=1
#=================for Water=================
  elif user_choice=='w':
    if comp_choice=='s':
      print("\nHard Luck!\nTry Again")
      score-=1
    elif comp_choice=='g':
      print("\nCongratulations!\nYou Wons")
      score+=1
#=================for Gun=================
  elif user_choice=='g':
    if comp_choice=='s':
      print("\nCongratulations!\nYou Won")
      score+=1
    elif comp_choice=='w':
      print("\nHard Luck!\nTry Again")
      score-=1
 #------------------------------------    
  else:
    print("\nInvalid Key Entered!")
    
    
#-------------------All Done---------------
  print("Your Score is: ",score)
  return True

while True:
  if not  play_game():
    break