"""8 queens puzzle"""

def conflict(board, i):
    n = len(board)
    cur_pos = board[i] # Compare all other positions to this

    # Scan vertically
    for pos in board[:i]:
        if pos == cur_pos:
            # This means we are in the same column
            print '|'
            return True

    # Scan diagonally
    for row, pos in enumerate(board[:i]):
        # Depending on which row we're comparing to, there can be a conflict
        if abs(row-i)==abs(cur_pos-pos):
            # We have a conflict
            print '\\'
            return True

    # Horizontal is assumed clear, since we only try rows with one queen in them
    print 'no conflict'
    return False

def solve_board(board):
    n = len(board)
    i = 0
    while i < n:
        # Try incrementing the position of the queen in this row
        board[i] += 1

        # See if there are any conflicts
        pos = board[i]
        if pos+1 > n:
            # We've reached the edge of the board, so we should backtrack
            print 'backtrack'
            board[i] = -1 # Remove queen from row
            i -= 1
        elif not conflict(board, i):
            i += 1

        print_board(board)

    return board

def print_board(board):
    for pos in board:
        if pos >= 0:
            print ''.join(['-'*pos]+['Q']+['-'*(len(board)-pos-1)])
        else:
            print ''.join(['-']*len(board))
    print ''

def main():
    n = 8
    empty_board = [-1]*n
    solved_board = solve_board(empty_board)

if __name__ == '__main__':
    main()
