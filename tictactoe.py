
def initialize_game():

    """
    Players choose their symbol an the game begins

    The format of the board is

            |       |
        7   |   8   |   9
            |       |
    -------------------------
            |       |
        4   |   5   |   6
            |       |
    -------------------------
            |       |
        1   |   2   |   3
            |       |

    """

    print('Welcome to Tic Tac Toe game! Have Fun!\n')

    player1 = input('Player 1, choose your symbol (it has to be X or O): ')
    while (not player1 == 'X') and (not player1 == 'O'):
        player1 = input('Please select one of the given symbols (X or O): ')

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return player1,player2


def board(dict_of_rows):

    """
    This function prints the tic tac toe board everytime a player plays. It takes as parameter the dictionary of every box.
    """

    print ('\n\n{}\n{}|{}|{}\n{}\n{}\n{}\n{}|{}|{}\n{}\n{}\n{}\n{}|{}|{}\n{}\n\n'.format(dict_of_rows[0],dict_of_rows[7],dict_of_rows[8],dict_of_rows[9],dict_of_rows[0],dict_of_rows['divider'],
                                                                                   dict_of_rows[0],dict_of_rows[4],dict_of_rows[5],dict_of_rows[6],dict_of_rows[0],dict_of_rows['divider'],
                                                                                   dict_of_rows[0],dict_of_rows[1],dict_of_rows[2],dict_of_rows[3],dict_of_rows[0]))


def pl_move(player):

    """
    This function checks if the given box by the players is permitted and returns this number of box. It takes as parameter the player who plays each turn.
    """

    print("It's Player {}'s turn".format(player))
    box = int(input('Where do you want to put your symbol??? '))
    while (box not in range(1,10)) or (box  in alr_pl):
        if box not in range(1,10):
            print('\n')
            print('Number {} is not between 0 and 9.'.format(box))
            box = int(input('Please select a number between 1 and 9: '))
            continue

        if box  in alr_pl:
            print('\n')
            print('Number {} has already been selected.'.format(box))
            box = int(input('Please select a different number: '))
            continue
    alr_pl.append(box)
    return box
    

def change_dict(dict_of_rows, player, box):

    """
    This function changes each box selected by player. It takes as parameters the dictionary of every box, the player and the number of box. 
    """

    if player == 'X':
        dict_of_rows[box] = '    X   '
    else:
        dict_of_rows[box] = '    O   '


def check_winner(player):

    """
    This function checks if we have a winner or a tie. It takes as parameter the player.
    """

    if  (dict_of_rows[1] == dict_of_rows[4] == dict_of_rows[7] != '        ') or (dict_of_rows[2] == dict_of_rows[5] == dict_of_rows[8] != '        ') or (dict_of_rows[3] == dict_of_rows[6] == dict_of_rows[9] != '        ') or (dict_of_rows[1] == dict_of_rows[2] == dict_of_rows[3] != '        ') or (dict_of_rows[4] == dict_of_rows[5] == dict_of_rows[6] != '        ') or (dict_of_rows[7] == dict_of_rows[8] == dict_of_rows[9] != '        ') or (dict_of_rows[1] == dict_of_rows[5] == dict_of_rows[9] != '        ') or (dict_of_rows[7] == dict_of_rows[5] == dict_of_rows[3] != '        '):
        print('Congratulations! Player {} is the winner!'.format(player))
        return True
    if len(alr_pl) == 9:
        print('We have a tie.. :(')
        return True



while True:
    dict_of_rows = {7: '        ',8: '        ',9: '        ',
                    4: '        ',5: '        ',6: '        ',
                    1: '        ',2: '        ',3: '        ',
                    0: '        |        |         ',
                    'divider': '---------------------------'}

    pl1, pl2 = initialize_game()
    print('Player 1 has the {} and Player 2 has the {}'.format(pl1, pl2))
    
    alr_pl = [] #the boxes which have already been selected
    board(dict_of_rows)
    while True:
        box = pl_move(1)
        change_dict(dict_of_rows,pl1,box)
        board(dict_of_rows)
        check = check_winner(1)
        if (check == True):
            break
        box = pl_move(2)
        change_dict(dict_of_rows,pl2,box)
        board(dict_of_rows)
        check = check_winner(2)
        if (check == True):
            break

    play_again = input('Do you want to play again? Y or N: ')
    while (not play_again == 'Y') and (not play_again == 'N'):
        play_again = input('Select one of the given options Y or N: ')
    if play_again == 'N':
        break