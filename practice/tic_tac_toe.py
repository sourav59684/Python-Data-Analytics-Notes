# =============================================================
# PROJECT : TIC TAC TOE
# A simple 2-player Tic Tac Toe game played in the console.
# =============================================================


def print_board(board_list):
    # Displays the current state of the board in a 3x3 grid
    print(f"\t\t {board_list[0]}   |\t{board_list[1]}  |\t{board_list[2]}")
    print("\t\t ----------------")
    print(f"\t\t {board_list[3]}   |\t{board_list[4]}  |\t{board_list[5]}")
    print("\t\t ----------------")
    print(f"\t\t {board_list[6]}   |\t{board_list[7]}  |\t{board_list[8]}")


def play_game():
    # Board positions are numbered 1-9 to start; each gets replaced
    # with 'x' or 'o' once a player picks that spot.
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_player = 'x'
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6)               # diagonals
    ]

    while True:
        print_board(board_list)
        print(f"Player {current_player}'s turn: ", end="")

        try:
            position = int(input())
        except ValueError:
            print("Please enter a number between 1-9, try again.")
            continue

        if position in board_list:
            board_list[position - 1] = current_player
            game_won = False

            for a, b, c in winning_combinations:
                if board_list[a] == board_list[b] == board_list[c]:
                    game_won = True
                    break

            if game_won:
                print(f"Player {current_player} wins the game!")
                print_board(board_list)
                return

            # if every cell has been replaced with 'x'/'o', it's a draw
            if all(isinstance(val, str) for val in board_list):
                print("It's a draw!")
                print_board(board_list)
                return

            current_player = 'o' if current_player == 'x' else 'x'
        else:
            print("Invalid input or spot already taken, try again.")


def main():
    print("\n\t\t Welcome to Tic Tac Toe")
    while True:
        play_game()
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
