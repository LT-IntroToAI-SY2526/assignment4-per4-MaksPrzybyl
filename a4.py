# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    def __init__(self):
        # Create a board with 9 empty spots
        self.board = ["*"] * 9

    def __str__(self) -> str:
        return (
            f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n"
            f"{self.board[3]} | {self.board[4]} | {self.board[5]}\n"
            f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        )
    def make_move(self, player: str, pos: int) -> bool:
        if pos not in range(9):  # invalid number
            return False
        if self.board[pos] != "*":  # already taken
            return False

        self.board[pos] = player
        return True
    def has_won(self, player: str) -> bool:
        """Return True if the given player has 3 in a row"""
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]

        return any(all(self.board[i] == player for i in combo)
                   for combo in winning_positions)
    def is_full(self)-> bool:
        return "*" not in self.board
    def game_over(self)-> bool:
        return self.has_won("X") or self.has_won("O") or self.is_full()
    def clear(self)-> None:
        self.board =["*"] * 9



def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


"""if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")


    play_tic_tac_toe()
pass"""

if __name__ == "__main__":
    brd = TTTBoard()
    print(brd)

    brd.make_move("X", 4)
    print(brd)

    brd.make_move("O", 4)  # try placing on taken spot (should fail)
    print(brd)
if __name__ == "__main__":
    brd = TTTBoard()
    brd.make_move("X", 0)
    brd.make_move("X", 1)
    brd.make_move("X", 2)
    print(brd)
    print("X wins?", brd.has_won("X"))  # should be True
    print("O wins?", brd.has_won("O"))  # should be False
if __name__ == "__main__":
    brd = TTTBoard()
    brd.make_move("X", 0)
    brd.make_move("X", 1)
    brd.make_move("X", 2)
    print(brd)
    print("Game Over?", brd.game_over())  # True
    print("Board Full?", brd.is_full())  # False
if __name__ == "__main__":
    brd = TTTBoard()
    brd.make_move("O", 0)
    print(brd)
    brd.clear()
    print(brd)  # should be all *