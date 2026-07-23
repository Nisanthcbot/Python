# take this program to run as a function when it is called 
"""
  - Define a functiom
  - Call the function 

"""

def number_guessing_game():

    import random
    secret_number = random.randint(1,100)

    print("Welcome To Number Gussing Game !")
    print("Guess the number Between 1-100")

    for i in range(1,8):
        try:
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
        except ValueError :
            print("Invalid Charater , Pls Enter 1-100")

    if secret_number == user_guessed :
        print(f"Congradulation You Find {secret_number} in {i} Attempts")

    else:
        print(f"Sorry Your Try is Over can u Try Again ! and the secret Number is : {secret_number}20")



print(number_guessing_game())