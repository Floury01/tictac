def field(board:list):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print('-----------')
            
def checkwin(board):
    win_comb=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [3, 4, 6]]
    for combo in win_comb:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    return " " not in board