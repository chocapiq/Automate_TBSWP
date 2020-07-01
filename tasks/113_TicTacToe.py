theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)
token = 'O'

def move(move, board):
    global token
    i = 0
    try:
        while i < 1:
            if board[move] is not ' ':
                print('Wrong move')
                i += 1
            else:
                board[move] = token
                if token == 'O':
                    token = 'X'
                else:
                    token = 'O'
                break
    except:
        print('Wrong command.')

def winConditions(board):
    while True:
        if board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O':
            print('O won!')
            break
        elif board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
            print('X won!')
            break
        elif board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O':
            print('O won!')
            break
        elif board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X':
            print('X won!')
            break
        elif board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O':
            print('O won!')
            break
        elif board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X':
            print('X won!')
            break
        elif board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O':
            print('O won!')
            break
        elif board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X':
            print('X won!')
            break
        elif board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O':
            print('O won!')
            break
        elif board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X':
            print('X won!')
            break
        elif board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O':
            print('O won!')
            break
        elif board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X':
            print('X won!')
            break
        elif board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O':
            print('O won!')
            break
        elif board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
            print('X won!')
            break
        elif board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O':
            print('O won!')
            break
        elif board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X':
            print('X won!')
            break
        elif board['top-R'] != ' ' and board['top-M'] != ' ' and board['top-L'] != ' ' and board['mid-R'] != ' ' and board['mid-M'] != ' ' and board['mid-L'] != ' ' and board['low-R'] != ' ' and board['low-M'] != ' ' and board['low-L'] != ' ':
            print("It's a draw!")
            break
        else:
            print('It is turn for ' + str(token))
            x = input()
            move(x, theBoard)
            printBoard(theBoard)

winConditions(theBoard)