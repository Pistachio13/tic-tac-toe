# take input
print(">>>>>tic tac toe winner checker")
print(">>>>>insert from left to right and above to below")

try:  
    board = []    
    for i in range(3):          
        r =[]
        for j in range(3):      
             r.append(int(input("insert: ")))
        board.append(r)
  
    for i in range(3):
        for j in range(3):
            print(board[i][j], end = " ")
        print()
except ValueError: 
        print("Null")
        exit()


# check row for win 
if board[0][0] == board[0][1] == board[0][2] and board[0][0] != 0:
    if board[0][0] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()
elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != 0:
    if board[1][0] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()
elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != 0:
    if board[2][0] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()


# check collumn for win 
if board[0][0] == board[1][0] == board[2][0] and board[0][0] != 0:
    if board[0][0] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()
elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != 0:
    if board[0][1] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()
elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != 0:
    if board[0][2] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()


# check diagonal for win 
if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
    if board[0][0] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()
elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0:
    if board[2][0] == 1:
        print("X win") 
    else:
        print("O win") 
    exit()

else:
    print("Draw")




