#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run pawn-brotherhood

# Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules.
# It has various units with a wide range of movement patterns allowing for a huge number of possible different game
# positions (for exampleNumber of possible chess games at the end of the n-th plies.) For this mission, we will
# examine the movements and behavior of chess pawns.
# 
# Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted
# with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of
# the chessboard is identified by a unique coordinate pair  — a letter and a number (ex, "a1", "h8", "d6").
# For this mission we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square
# diagonally in front of it on an adjacent file, by moving to that square. For white pawns the front squares are
# squares with greater row number than the square they currently occupy.
# 
# A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
# With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
# We have several white pawns on the chess board and only white pawns. You should design your code to find how many
# pawns are safe.
# 
# 
# 
# You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.
# 
# Input:Placed pawns coordinates as a set of strings.
# 
# Output:The number of safe pawns as an integer.
# 
# Precondition:
# 0 < pawns ≤ 8
# 
# 
# END_DESC


def safe_pawns(pawns: set) -> int:
    safe_count = 0

    # create a new set to put the individual positions in integer form
    pawns_positions = set()

    # get row and column for each entry
    for p in pawns:
        row = int(p[1])
        column = ord(p[0])
        # add the new position to the position set
        pawns_positions.add((row, column))

    # iterate over each of the positions to see if it is a safe position
    for row, column in pawns_positions:
        safe_position = ((row - 1, column - 1) in pawns_positions) or ((row - 1, column + 1) in pawns_positions)
        if safe_position:
            safe_count += 1

    return safe_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
