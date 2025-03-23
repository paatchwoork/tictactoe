# Draws the board
def draw_board (spots):
    board = (f"{spots[1]}|{spots[2]}|{spots[3]}\n"
    f"{spots[4]}|{spots[5]}|{spots[6]}\n"
    f"{spots[7]}|{spots[8]}|{spots[9]}\n")
    print(board)

# Returns the player number and its corresponding checkmark
def check_turn (turn):
    if turn%2 == 0:
        return ["2","X"]
    else :
        return ["1","O"]

# Evaluates if there is a win or a draw, and returns nothing is neither
def evaluate(spots):
    if spots[1] == spots[2] == spots[3] or \
    spots[4] == spots[5] == spots[6] or \
    spots[7] == spots[8] == spots[9] or \
    spots[1] == spots[4] == spots[7] or \
    spots[2] == spots[5] == spots[8] or \
    spots[3] == spots[6] == spots[9] or \
    spots[1] == spots[5] == spots[9] or \
    spots[3] == spots[5] == spots[7] :
        return True
    elif set(spots.values()) == {"X","O"}:
        return False