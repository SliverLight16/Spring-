import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #rock is 0 , paper is 1, scissors is 2
    computer_pick = options[random_number]
    print(f'Computer picked {computer_pick}.')

    if user_input == "rock" and computer_pick == "scissors":
        print("You Win")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win")
        user_wins += 1

#insurance against ties
    elif user_input == "rock" and computer_pick == "rock":
        print("Tie")

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Tie")

    elif user_input == "paper" and computer_pick == "paper":
        print("Tie")     

    else:
        print("You lost!")
        comp_wins += 1

if comp_wins > user_wins:
    print(f"The computer wins {comp_wins} to {user_wins}")

elif comp_wins == user_wins:
    print("Its a tie!")

else:
    print(f'You win {user_wins} to {comp_wins} \nCongrats')




