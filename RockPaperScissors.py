import random

# In this first part, both players enter their names. I made a list of their names and then I made that list random.

p1_name = input('Player 1, please enter your name: ')
p2_name = input('Player 2, please enter your name: ')
mylist = [p1_name, p2_name]
mylist_random = random.sample(mylist, 2)

# This part, the game is running.

while True:

    # I picked the first and second elements of the random list and assiged them to the variables turn and turn2.
    # I did that in order to assign the randomly chosen first player to his turn.

    turn = mylist_random[0]
    turn2 = mylist_random[1]
    print(turn + ' will start first')
    player1_choice = input(turn + ' choose rock, paper, or scissors. Use R for rock, P for paper, or S for scissors: ').lower()
    player2_choice = input(turn2 + ' choose rock, paper, or scissors. Use R for rock, P for paper, or S for scissors: ').lower()

    # The first if statement depicts a tie.
    # The players will always be asked if they want to play again or not.
    # If they choose not to play, the game in gonna prompt a message saying game over.

    if player1_choice == player2_choice:
        print('It is a tie!')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break

    # This elif statement depicts one game situation, as the other elif statements as well.

    elif player1_choice == 'r' and player2_choice == 'p':
        print(p2_name + ' won the game!')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif player1_choice == 'r' and player2_choice == 's':
        print(p1_name + ' won the game!')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif player2_choice == 'r' and player1_choice == 'p':
        print(p1_name + ' won the game!')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif player2_choice == 'r' and player1_choice == 's':
        print(p2_name + ' won the game!')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    # The pass is to cover any other possible situation that is not relevant to the game.

    else:
        pass
