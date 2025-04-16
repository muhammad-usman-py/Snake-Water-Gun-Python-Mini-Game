#Taking usr iphut S W G
# computer will choose S W G
# Game Rules
# 1. The computer will choose S, W, or G randomly.
# 2. The user will choose S, W, or G.
"""                        -1 0 1
computer chooses            S w G
user chooses         -1 S   D W L
                     0  W   L D W
                     1  G   W L G
"""

#Coding
import random
while True:
    #1. The computer will choose S, W, or G randomly.
    computer_choice = random.choice(['S', 'W', 'G'])

    print(f"Computer chose {computer_choice}")

    # 2. The user will choose S, W, or G.
    user_choice = input("Enter your choice (S for Snake, W for Water, G for Gun): ").upper()

    if user_choice not in ['S', 'W', 'G']:
        print("Invalid input. Please enter only S, W, or G.")
        continue
    
    print(f"\nYou chose {user_choice}, Computer chose {computer_choice}")
    print("--- Result ---")

    #results
    if computer_choice==user_choice:
        print("It's a tie!")
    elif (user_choice == 'S' and computer_choice == 'W') or \
         (user_choice == 'W' and computer_choice == 'G') or \
         (user_choice == 'G' and computer_choice == 'S'):
        print("You win!")
    else:
        print("You lose!")
        
    # Ask to play again
    again = input("Play again? (Y/N): ").upper()
    if again != 'Y':
        print("Thanks for playing!")
        break
