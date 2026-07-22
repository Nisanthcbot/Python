#Print is the number gussed number is right or not with of 7 trials.


secret_number = 56


# using for loop

for i in range(1,8):

    user_guessed = int(input("Enter Your Guessed Number :"))

    if secret_number == user_guessed :
        print("Congradulation Your Guess is right")
        break
    else:
        print("Sorry, Your Guessed is Wrong!")



#While loop - when the number of instruction has to executed infinite time :

while True:

    user_guessed = int(input("Enter Your Guessed Number :"))

    if secret_number == user_guessed :
        print("Congradulation Your Guess is right")
        break
    else:
        print("Sorry, Your Guessed is Wrong!")  