# import random

# name=input("Enter Your Name : ")
# system_number=random.randint(1,20)

# print(f"\nWelcome {name}! Let's play a game !")
# print("I, the system have selected a number between 1 to 20 ! ")
# print("You have 6 attempts to guess the number selected by me !")

# attempts=0

# while attempts<6:
#     guess=int(input("Enter your guessed number : "))
#     attempts=attempts + 1 

#     if guess<system_number:
#         print("Your Guess Is TOO LOW !")
#     elif guess>system_number:
#         print("Your Guess Is TOO HIGH !")
#     else:
#         print(f"Congratulations {name}! YOU GUESSED RIGHT!!")
#         print("YOU WON THE GAME !")
#         break

# if guess!=system_number:
#     print("\nGAME OVER ! YOU LOST THE GAME !!!!!!!!")
#     print(f"The Correct Answer was {system_number} !!")
#     print(f"BETTER LUCK NEXT TIME {name}!!")