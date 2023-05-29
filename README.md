# Tic-Tac-Toe using Minimax with Alpha-Beta Pruning

This is a Python implementation of the game Tic-Tac-Toe, where you can play against the computer. The computer uses the Minimax algorithm with Alpha-Beta pruning to make its moves.

## Instructions

1. Run the program using Python.
2. The game will start, and you will be asked to choose whether you want to play first (as 'X') or second (as 'O').
3. Enter '1' to play first or '2' to play second and press Enter.
4. The game board will be displayed, and the empty cells are marked with numbers from 1 to 9.
5. Each number represents a position on the board as follows:

```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
```

6. To make a move, enter the corresponding number of the position you want to mark and press Enter.
7. The computer will make its move immediately after you make yours.
8. The game continues until either one of the players wins or the game ends in a draw.
9. Once the game ends, the result will be displayed, indicating whether 'X' or 'O' has won or if it's a draw.
10. You can choose to play again by running the program again.

## Requirements

- Python 3.x

## Code Explanation

The code is divided into several functions to handle different aspects of the game:

- `printBoard(board)`: Prints the game board with the current marks.
- `clearBoard(board)`: Resets the game board by setting all cells to empty.
- `hasPlayerWon(board, player)`: Checks if a player has won the game based on the current board configuration.
- `isGameWon(board)`: Checks if either player has won the game.
- `printResult(board)`: Prints the result of the game (win/lose/draw).
- `getBlanks(board)`: Returns a list of empty cells on the board.
- `isBoardFull(board)`: Checks if the board is full and no more moves can be made.
- `makeMove(board, x, y, player)`: Makes a move by marking a cell with the player's mark.
- `playerMove(board)`: Handles the player's move by getting input and making the corresponding move.
- `getScore(board)`: Assigns a score to the current board configuration based on whether a player has won or not.
- `alphaBetaMinimax(board, depth, alpha, beta, player)`: Implements the Minimax algorithm with Alpha-Beta pruning to determine the best move for the computer player.
- `computerMove(board, player)`: Makes a move for the computer player using the Minimax algorithm.
- `playVsComputer()`: Handles the game flow between the player and computer.
- The program starts by printing a welcome message and then calls the `playVsComputer()` function to start the game.

## References

- Minimax algorithm: [https://en.wikipedia.org/wiki/Minimax](https://en.wikipedia.org/wiki/Minimax)
- Alpha-Beta pruning: [https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)