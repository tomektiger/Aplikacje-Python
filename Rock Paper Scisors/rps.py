#HELLO THIS IS ROCK PAPER SCISORS GAME CREATED BY TOMEKTIGER
import random

player1_score = 0
player2_score = 0

while True:

    print("...rock....")
    print("...paper....")
    print("...scisors....")



    player1_input = str(input("Player 1 Choose: ---> ").lower())

    list = ["rock", "paper", "scisors"]

    player2_choose = random.choice(list)

    print(f"Player 1 Played: {player1_input}")
    print(f"Player 2 Played: {player2_choose}")

    def play_game():
        if player1_input != "" and player2_choose != "":

            winner = None

            if player1_input == "rock" and player2_choose == "paper":
                winner = "Player 2"
            elif player1_input == "paper" and player2_choose == "scisors":
                winner = "Player 2"
            elif player1_input == "paper" and player2_choose == "rock":
                winner = "Player 1"
            elif player1_input == "scisors" and player2_choose == "rock":
                winner = "Player 2"
            elif player1_input == "rock" and player2_choose == "scisors":
                winner = "Player 1"
            elif player1_input == "scisors" and player2_choose == "paper":
                winner = "Player 1"
            elif player1_input == "scisors" and player2_choose == "scisors":
                winner = "Tie"
            elif player1_input == "rock" and player2_choose == "rock":
                winner = "Tie"
            elif player1_input == "paper" and player2_choose == "paper":
                winner = "Tie"
            return winner
        else:
            print("\nSomething went wrong")

    winner = play_game()

    print("\nSHOOOT")

    print(f"\nAND THE WINNER IS: {winner}")

    if winner == "Player 1":
        player1_score += 1
    elif winner == "Player 2":
        player2_score += 1

    if player1_score > player2_score:
        main_winner = "Player 1"
        high_score = player1_score
    else:
        main_winner = "Player 2"
        high_score = player2_score

    while True:
        answer = str(input('Chcesz zagrać ponownie ? (tak/nie): '))
        if answer in ('tak', 'nie'):
            break
        print("ZŁE WPROWADZENIE SŁOWA")
    if answer == 'tak':
        continue
    else:
        print(f"Gracze zdobyli:\n Player 1 : {player1_score} punkty\n Player 2: {player2_score} punkty")
        print(f"WYGRYWA {main_winner} z {high_score} PUNKTAMI ")
        break
