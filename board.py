def makeNewBoard(boardSize):
    # Creates a brand new, blank, board data structure
    board = []                      # type of board: list
    if isinstance(boardSize, int):  # if type(boardSize) == int:
        for i in range(boardSize):  # type of i: int
            line = [' '] * 8
            board.append(line)
        # the created board includes boardSize elements, each of type list
    return board
