theboard = {'7': '', '8': '' , '9': '',
            '4': '', '5': '', '6': '',
            '1': '', '2': '', '3': ''}
board_keys = []
for key in theboard:
    board_keys.append(key)
def printboard(board):
    print(board['7']+ '|'+board['8']+ '|'+board['9']+ '|')
    print('-------')
    print(board['4']+ '|'+board['5']+ '|'+board['6']+ '|')
    print('-------')
    print(board['1']+ '|'+board['2']+ '|'+board['3']+ '|')

def game():
    turn = 'x'
    count = 0

    for i in range(10):
        printboard(theboard)
        print("it is your turn" , turn , "Where do you want to place it?")

        move =input()
        if theboard[move] == '':
            theboard[move] = turn
            count += 1
        else:
            print("that place is already filled move to another place")
            continue
        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] !=  ' ': #across top
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['4'] == theboard['5']== theboard['6']== ' ':#across middle
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['1']== theboard['2']==theboard['3'] !='' :#across middle
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['1']== theboard['5']==theboard['9'] !='' :#bottom to top diagnolly
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['1']== theboard['4']==theboard['7'] !='' : #down left side
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['2']== theboard['5']==theboard['8'] !='' : #down middle
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['3']== theboard['6']==theboard['9'] !='' :#down right
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
            if theboard['7']== theboard['5']==theboard['3'] !='' : #diagonal
                printboard(theboard)
                print("Game over")
                print("------" , turn , "has won" , "-----")
        if count == 9:
            print("game over")
            print("it is a tie")

        if turn ==  'x':
            turn == 'O'
        else:
            turn == 'x'
restart = input("Do you want to play again?")
if restart == "yes" or "Yes":
    for key in board_keys:
        theboard[key] =  " "
    

    game()


if __name__ == "__main__":
    game()

