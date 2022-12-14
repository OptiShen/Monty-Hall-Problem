import random
import matplotlib.pyplot as plt
import time

global choice


# We are going with 3 doors :
# 1 - Car
# 2 - Goats
doors = ["goat", "goat", "car"]

# Empty lists to store probability values :
switch_win_probability = []
stick_win_probability = []

plt.axhline(y=0.66666, color='r', linestyle='-')
plt.axhline(y=0.33333, color='g', linestyle='-')

# inaayos ko pa
def choiceInput():
    while True:
        try:
            global choice
            choice = int(input("\nWhich door do you want to choose? (1,2,3): "))
            if choice == 1 or choice == 2 or choice == 3:
                print("You have chosen door number " + str(choice))
                break
            else:
                print("\nError: 1,2 or 3 only. Please try again.")
        except ValueError:
            print('\nError: 1,2 or 3 only. Please try again.')


def play_monty_hall(choice):
    # Prizes behind the door
    # initial ordering doesn't matter
    prizes = ['goat', 'car', 'goat']

    # Randomizing the prizes
    random.shuffle(prizes)

    # Determining door without car to open
    while True:
        opening_door = random.randrange(len(prizes))
        if prizes[opening_door] != 'car' and choice - 1 != opening_door:
            break

    opening_door = opening_door + 1
    time.sleep(1)
    print('The host opened the other door number %d' % (opening_door))

    # Determining switching door
    options = [1, 2, 3]
    options.remove(choice)
    options.remove(opening_door)
    switching_door = options[0]

    # Asking for switching the option

    while True:
        try:
            print("STAY or SWITCH only")
            print('Now, do you want to switch to door number %d or stay? [switch/stay]: ' % (switching_door))
            answer = str(input())
            if answer.lower() == 'switch':
                result = switching_door - 1
                break
            elif answer.lower() == 'stay':
                result = choice - 1
                break
        except ValueError:
            print("Please choose between switch or stay only.\n")

        # Displaying the player's prize
    print('You chose ' + answer + ', you got', prizes[result].upper())
    if result == "car":
        print("You WON bro :)\n")

# Monte_Carlo Simulation :
def monte_carlo():
    # Calculating switch and stick wins :
    switch_wins = 0
    stick_wins = 0

    while True:
        try:
            iteration_input = int(input("Please enter number of iterations: "))
            print("You have entered " + str(iteration_input))
            break
        except ValueError:
            print("Integers only\n")

    for i in range(iteration_input):

        # Randomly placing the car and goats behind the three doors :
        random.shuffle(doors)

        # Contestant's choice :
        k = random.randrange(2)

        # If the contestant doesn't get car :
        if doors[k] != 'car':
            switch_wins += 1

        # If the contestant got car :
        else:
            stick_wins += 1

        # Updating the list values :
        switch_win_probability.append(switch_wins / (i + 1))
        stick_win_probability.append(stick_wins / (i + 1))

        # Plotting the data :
        plt.plot(switch_win_probability)
        plt.plot(stick_win_probability)

        # Print the probability values :
    print('\nWinning probability if you always switch:', switch_win_probability[-1])
    print('Winning probability if you always stick to your original choice:', stick_win_probability[-1])


# Playing game
# displaying the name of game ;)
print(
    '________            _______    _____________   ______     ______   _______________   _______      _______                                    |')
print(
    '||     |           ||     |    ||          |   ||     | |     |   ||            |   ||    |      ||    |                                    |')
print(
    '||      |         ||      |    ||  _____   |   ||      ||     |   ||___      ___|    ||    |    ||    |                                     |')
print(
    '||       |       ||       |    ||  |   ||  |   ||       |     |       ||    |         ||    |  ||    |                                      |')
print(
    '||        |     ||        |    ||  |   ||  |   ||             |       ||    |          ||    |||    |                                       |')
print(
    '||         |   ||         |    ||  |   ||  |   ||    |\       |       ||    |           ||         |                                        |')
print(
    '||    |\    \//    /||    |    ||  |   ||  |   ||    | \      |       ||    |            ||       |                                         |')
print(
    '||    | \         / ||    |    ||  ------  |   ||    |  \     |       ||    |            ||       |                                         |')
print(
    '||____|  \_______/  ||____|    ||__________|   ||____|   \____|       ||____|            ||_______|                                         |')
print(
    '                                                                                                                                            |')
print(
    '_________     _________   ________________   ________         ________                  _____________    _____________    _____________     |')
print(
    '||      |     ||      |   ||             |   ||     |         ||     |                 ||  __   __  ||  ||  __   __  ||  ||  __   __  ||    |')
print(
    '||      |     ||      |   ||    _____    |   ||     |         ||     |                 ||  ||   ||  ||  ||  ||   ||  ||  ||  ||   ||  ||    |')
print(
    '||      |_____||      |   ||    |  ||    |   ||     |         ||     |                 ||  --   --  ||  ||  --   --  ||  ||  --   --  ||    |')
print(
    '||                    |   ||    |__||    |   ||     |         ||     |                 ||  0        ||  ||  0        ||  ||  0        ||    |')
print(
    '||       ______       |   ||             |   ||     |         ||     |                 ||  __   __  ||  ||  __   __  ||  ||  __   __  ||    |')
print(
    '||      |     ||      |   ||    -----    |   ||     -------   ||     -------           ||  ||   ||  ||  ||  ||   ||  ||  ||  ||   ||  ||    |')
print(
    '||      |     ||      |   ||    |  ||    |   ||           |   ||           |           ||  --   --  ||  ||  --   --  ||  ||  --   --  ||    |')
print(
    '||______|     ||______|   ||____|  ||____|   ||___________|   ||___________|           ||___________||  ||___________||  ||___________||    |')

# hall
print(
    '____________________________________________________________________________________________________________________________________________|')
print('')
print('')
print('')

print(' _____________      _____________      _____________')
print('||  __   __  ||    ||  __   __  ||    ||  __   __  ||')
print('||  ||   ||  ||    ||  ||   ||  ||    ||  ||   ||  ||')
print('||  --   --  ||    ||  --   --  ||    ||  --   --  ||')
print('||  0 (1)    ||    ||  0 (2)    ||    ||  0 (3)    ||')
print('||  __   __  ||    ||  __   __  ||    ||  __   __  ||')
print('||  ||   ||  ||    ||  ||   ||  ||    ||  ||   ||  ||')
print('||  --   --  ||    ||  --   --  ||    ||  --   --  ||')
print('||___________||    ||___________||    ||___________||')
print('')
choiceInput()
play_monty_hall(choice)



# Calling the function :
monte_carlo()
