# Give Multiple condition 
"""
  1) User should enter the numnber between 1-100 if its entered wrong, the pogram should say , invalid Number
  2) user Guessed number > secret number , then the program should say number Greaterthan Secret Number
  3) user Guessed number < secret number , then the program should say number Lesserthan Secret Number
  40 add print Fromating
"""

print("Welcome To Number Gussing Game !")
print("Guess the number Between 1-100")

secret_number = 56

for i in range(1,8):

    user_guessed = int(input("Enter Your Guessed Number :"))

    if user_guessed < 1 or user_guessed > 100:
        print("Invalid Number , Try Again!")

    elif user_guessed > secret_number:
        print("Greatertha Secret Number")

    elif user_guessed < secret_number:
        print("Lessethan Secret Number ")

    else:
        print("Congradulation Your Guess is right")
        print(f"Congradulation You Find {secret_number} in {i} Attempts")
        break
