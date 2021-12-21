import random
correct_number = random.randint(1, 10)
while True:
    guess_input = int(input("Guess the number between 1 and 10 : "))
    if guess_input != correct_number:
        print("WRONG ANSWER")
        if guess_input > correct_number:
            print("YOUR GUESS WAS TOO HIGH")
        else:
            print("YOUR GUESS WAS TOO LOW")
    if guess_input == correct_number:
        print("CORRECT ! YOU GUESSED GOOD")
        ask_input = input("DO YOU WANT TO PLAY AGAIN ? : yes/no \n")
        if ask_input == "yes":
            correct_number = random.randint(1, 10)
            continue
        else:
            break