'''
GuessingGame
Toaster914
10/17/22
'''

import random

again = "Y"
while again == "Y" or again == "y":
  num = random.randint(1, 100)
  #print(num) #for testing
  print("I am thinking of a number between 1 and 100.")
  print("Can you guess my number?")
  print()
  solved = False
  times = 0
  while solved == False:
    guess = int(input("What is your guess? >> "))
    if guess == num:
      times += 1
      print("You got the number of " + str(num) + "!")
      print("It took you " + str(times) + " guesses.")
      solved = True
      again = input("Would you like to play again? (Y/N) >> ")
      print()
    elif guess > 100 or guess < 1:
      print("That is outide the range!")
      print()
      times += 1
    elif guess < num:
      print("Too low!")
      print()
      times += 1
    elif guess > num:
      print("Too high!")
      print()
      times += 1
