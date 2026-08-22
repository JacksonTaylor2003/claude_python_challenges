def print_board(board:list):
    print()
    for i in range(3):
        row = board[(i*3):(i*3)+3]
        display_row = [str(val if val != " " else (i*3)+ind) for ind, val in enumerate(row)]
        print(" | ".join(display_row))
        if i < 2:
            print ("-----------")
    print()

def check_winner(board):
    winning_lines = [
        [0,1,2], [3,4,5], [6,7,8], #rows
        [0,3,6], [1,4,7], [2,5,8], #columns
        [0,4,8], [2,4,6]           #diagonals
    ]
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]
    return None

def switch_player(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"

def play_game():
    play_again = True

    while play_again:

        board = [" "] * 9
        current_player = "X"
    
        print("\033[H\033[J", end="")
        print_board(board)

        while True:
            try:
                player_input = int(input(f"{current_player}'s turn. Choose a spot\n>>> "))
            except ValueError as e:
                print("Please select a number")
                continue

            
            if player_input > 8 or player_input < 0:
                print("Please select a valid number.")
                continue
            elif board[player_input] != " ":
                print("Please select an empty space")
                continue
            else:
                board[player_input] = current_player

            print("\033[H\033[J", end="")

            print_board(board)

            winner = check_winner(board)
            
            if winner:
                print(f"{winner} has won the game!")
                break

            if not " " in board:
                print("Tie!")
                break

            current_player = switch_player(current_player)

        while True:
            try:
                user_input = int(input("Would you like to play again? Yes(1) | No(0)\n>>> "))
            except ValueError as e:
                print("Please select a valid option")
                continue

            if user_input == 1:
                break
            elif user_input == 0:
                play_again = False
                break
            else:
                print("Please select a valid option")
                continue


#Start Game
play_game()