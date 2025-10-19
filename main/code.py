def field(board:list):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print('-----------')
            
