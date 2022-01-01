import time
import random

wlc = False # One-time welcome message
yc = 0 # Your Choice
bc = 0 # Bot's Choice
# ^ You can't put a NoneType or a String because it will result in an error 

x = 0 # Later on
chk = 0 # Later on
bot_choice = [
  ["Rock", "Paper", "Scissors"],
  ["Rock", "Paper", "Scissors"],
  ["Rock", "Paper", "Scissors"]
]
your_choice = [
  "Rock",
  "Paper",
  "Scissors"
]


print("Hi, welcome to a \"normal\" Rock Paper Scissors game!\n")
time.sleep(1) # This is a one-time welcome message

def game():

    you_choose() # Your choice
  
    choosing() # Bot's choice depending on your choice

    checking_and_improoving() # Checking who won; if the bot won, moving on, otherwise the bad option will be removed from the list of bot's choices (couldn't find a shorter name)

    again() # Wanna go again?

def you_choose():
  global yc
  
  yc = input("""\nWhat will your choice be?
1. Rock
2. Paper
3. Scissors
\n""")
  while yc not in ["1","2","3"]:
    print(f"\n{yc} is not a choice!\n")
    yc = input("""What will your choice be?
1. Rock
2. Paper
3. Scissors
\n""")

def choosing():
  global yc
  global bc
  global x
  global chk
  
  yc = int(yc)
  bc = yc - 1
  chk = bc
  yc = your_choice[yc - 1]

  x = random.randint(0,len(bot_choice[chk]) - 1)
  bc = bot_choice[bc][x]

def checking_and_improoving():
  global yc
  global bc
  global x
  global chk

  if yc == "Rock":
    print("You chose ROCK")
    
    if bc == "Rock":
      print("The bot chose ROCK")
      time.sleep(1)
      print("\nIT'S A TIE!\n")
      bot_choice[chk].remove(bc)
      
    if bc == "Paper":
      print("The bot chose PAPER")
      time.sleep(1)
      print("\nYOU LOSE!\n")
      
    if bc == "Scissors":
      print("The bot chose SCISSORS")
      time.sleep(1)
      print("\nYOU WIN!\n")
      bot_choice[chk].remove(bc)

      
  if yc == "Paper":
    print("You chose Paper")
    
    if bc == "Rock":
      print("The bot chose ROCK")
      time.sleep(1)
      print("\nYOU WIN!\n")
      bot_choice[chk].remove(bc)
      
    if bc == "Paper":
      print("The bot chose PAPER")
      time.sleep(1)
      print("\nIT'S A TIE!\n")
      bot_choice[chk].remove(bc)
      
    if bc == "Scissors":
      print("The bot chose SCISSORS")
      time.sleep(1)
      print("\nYOU LOSE!\n")

      
  if yc == "Scissors":
    print("You chose SCISSORS")
    
    if bc == "Rock":
      print("The bot chose ROCK")
      time.sleep(1)
      print("\nYOU LOSE!\n")
      
    if bc == "Paper":
      print("The bot chose PAPER")
      time.sleep(1)
      print("\nYOU WIN!\n")
      bot_choice[chk].remove(bc)
      
    if bc == "Scissors":
      print("The bot chose SCISSORS")
      time.sleep(1)
      print("\nIT'S A TIE!\n")
      bot_choice[chk].remove(bc)
      

def again():
  againn = input("""Want to go again?
1. Yes
2. No
""")
  while againn not in ["1", "2"]:
    print(f"\n{againn} is not an option!\n")
    againn = input("""Want to go again?
1. Yes
2. No
""")
  if againn == "1":
    game()
  else:
    print("It was nice playing with you ;)\nGoodbye!")
    return
      

#print("bc = ", bc)
#print("chk = ",chk)
#print("x = ", x)
#print(bot_choice[chk])
#print(bot_choice[chk][x])

# Don't mind this stuff ^
game()
