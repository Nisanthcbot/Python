# Setting Multiple Conditions
"""
   1) if the try is over the system should say . Sorry you try is over can u try again!
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
        break

if secret_number == user_guessed :
    print(f"Congradulation You Find {secret_number} in {i} Attempts")

else:
    print("Sorry Your Try is Over can u Try Again !")