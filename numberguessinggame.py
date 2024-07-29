import random

while True: 

    print ("Guess a number in between 1 - 100.")

    computer_number = random.randint(1,100) #randint is to put a range in between random numbers

    while True:
        user_input = input("Enter your guess:")

        user_guess = int(user_input)
        
        if user_guess == computer_number:
            print("You're a wizard Harry!")
            break
        elif user_guess < computer_number:
            print("Higher!")
        else: 
            print("Lower!")

    again = input ("Again? Y/N:")
    if again != "y":
        print ("Goodbye")
        break