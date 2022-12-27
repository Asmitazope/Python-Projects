
# function to return sum
def sum(a, b, c):
    return a + b + c

# function to print the board for Tic Tac Toe

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0 )
    one = 'X' if xState[1] else ('O' if zState[1] else 1 )
    two = 'X' if xState[2] else ('O' if zState[2] else 2 )
    three = 'X' if xState[3] else ('O' if zState[3] else 3 )
    four = 'X' if xState[4] else ('O' if zState[4] else 4 )
    five = 'X' if xState[5] else ('O' if zState[5] else 5 )
    six = 'X' if xState[6] else ('O' if zState[6] else 6 )
    seven = 'X' if xState[7] else ('O' if zState[7] else 7 )
    eight = 'X' if xState[8] else ('O' if zState[8] else 8 )

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|--")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight} ")
    print(f"--|---|--")

# function to check who wins the game X or O

def checkWin(xState, zState):

    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print('\r')
            print('----X Won The Game----')
            print('\r')
            return 1

        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print('\r')
            print('----O Won The Game-----')
            print('\r')
            return 0
    return -1

# Driver Mode

if __name__ == "__main__":

    # states
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    turn  = 1   # 1 for X and 0 for o

    print("Welcome to Tic Tac Toe ! \n ")

    while True:
        printBoard(xState, zState)

        if turn == 1:
            print('\r')
            print("X's Chance \n")
            value = int(input("Please enter a value: "))
            print('\r')
            xState[value] = 1
        
        else:
            print("\r")
            print("O's Chance \n")
            value = int(input("Please enter a value: "))
            print('\r')
            zState[value] = 1

        cwin = checkWin(xState, zState)

        if cwin != -1:
            print('\r')
            print('Match Over')
            print('\r')
            print('Thank You For PLaying :)')
            print('\r')
            break

        turn = 1 - turn

        

