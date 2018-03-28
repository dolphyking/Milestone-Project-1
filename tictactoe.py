test_list = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
acceptables = [1,2,3,4,5,6,7,8,9]
turn = 2


def display_board(board):

    # Draws the board with updated values

    print('     |     |     ')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |     ')
    print('-----|-----|-----')
    print('     |     |     ')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |     ')
    print('-----|-----|-----')
    print('     |     |     ')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |     ')


def clear_output():

    # Prints 100 new lines

    print('\n'*100)


def num_input():

    # Accepts a certain range of inputs (1-9)

    while True:
        try:
            x = int(input('Enter values 1-9 here: '))
        except ValueError:
            print("It's not a number, fuckface!")
            continue
        if x in acceptables and test_list[x] == ' ':
            return x


def assign_input(turn, test_list):

    # Assigns input to a position in the list

    z = num_input()

    if turn % 2 == 0:
        test_list[z] = 'X'
        return test_list
    else:
        test_list[z] = '0'
        return test_list


def check_wincon(test_list):

    # Tests for certain win conditions (based on rules of tic-tac-toe)

    if test_list[7] == test_list[4] == test_list[1] != ' ':
        print(f'Congratulations! {test_list[7]} wins the game!')
        return True
    elif test_list[8] == test_list[5] == test_list[2] != ' ':
        print(f'Congratulations! {test_list[8]} wins the game!')
        return True
    elif test_list[9] == test_list[6] == test_list[3] != ' ':
        print(f'Congratulations! {test_list[9]} wins the game!')
        return True
    elif test_list[7] == test_list[8] == test_list[9] != ' ':
        print(f'Congratulations! {test_list[7]} wins the game!')
        return True
    elif test_list[4] == test_list[5] == test_list[6] != ' ':
        print(f'Congratulations! {test_list[4]} wins the game!')
        return True
    elif test_list[1] == test_list[2] == test_list[3] != ' ':
        print(f'Congratulations! {test_list[1]} wins the game!')
        return True
    elif test_list[1] == test_list[5] == test_list[9] != ' ':
        print(f'Congratulations! {test_list[1]} wins the game!')
        return True
    elif test_list[7] == test_list[5] == test_list[3] != ' ':
        print(f'Congratulations! {test_list[7]} wins the game!')
        return True
    return False


# //MAIN BODY(LOOP)


while not check_wincon(test_list) and turn != 11:
    assign_input(turn, test_list)
    clear_output()
    display_board(test_list)
    check_wincon(test_list)
    turn += 1
    if test_list.count(' ') == 0 and check_wincon(test_list) == False:
        print('You both lose.')
        exit()
