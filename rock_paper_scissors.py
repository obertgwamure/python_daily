from getpass import getpass as input

dict_choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
dict_results = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}


def get_input(player):
    while True:
        try:
            inp = input(
                f'Player {player} Enter:\nR for rock\nP for paper\nS for scissors: \n\n\n'
            )
            if inp.lower() in dict_choices:
                return dict_choices[inp.lower()]
            else:
                print('Invalid input')
        except:
            print('Invalid input')


def main():
    inp_1 = get_input(1)
    inp_2 = get_input(2)
    print(f'Player 1 chose {inp_1} X Player 2 chose {inp_2}')
    if inp_1 == inp_2:
        print('It\'s a tie')
    elif dict_results[inp_1] == inp_2:
        print('Player 2 wins!')
    else:
        print('Player 1 wins!')


main()

