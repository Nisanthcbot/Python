#Print is the number gussed number is right or not.

secret_number = 56

user_guessed = int(input("Enter Your Guessed Number :"))

if secret_number == user_guessed :
    print("Congradulation Your Guess is right")
else:
    print("Sorry, Your Guessed is Wrong!")