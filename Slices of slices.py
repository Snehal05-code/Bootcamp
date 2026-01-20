def main():
    
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    
    board[0][0] = "X"
    board[2][2] = "O"
    board[1][2] = "X"
    board[1][0] = "O"
    board[0][2] = "X"

    
    for i in range(len(board)):
        print(" ".join(board[i]))

main()

	