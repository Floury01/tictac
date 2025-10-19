def field(board:list):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]}")
        if i < 2:
            print('-----------')
            
def checkwin(board):
    win_comb=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in win_comb:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def is_board_full(board):
    return " " not in board

def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    print("Добро пожаловать в Крестики-нолики!")
    print("Для хода введите число от 1 до 9:")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print()
    
    while True:
        field(board)
        print(f"\nХод игрока {current_player}")
        
        try:
            move = int(input("Введите номер клетки (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Пожалуйста, введите число от 1 до 9!")
                continue
                
            if board[move] != " ":
                print("Эта клетка уже занята!")
                continue
                
        except ValueError:
            print("Пожалуйста, введите число!")
            continue
        
        board[move] = current_player
        
        winner = checkwin(board)
        if winner:
            field(board)
            print(f"\nПобедил игрок {winner}!")
            break
            
        if is_board_full(board):
            field(board)
            print("\nНичья!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
    