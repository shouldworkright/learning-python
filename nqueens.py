
'''
    Python solution for the 'N-Queens' problem for a
    user-selected number of queens.
    Author: Dan Mello
    Version: 1.0
    Date: 2019-17-11
''' 

# Prompt user to enter desired number of queens.
print ("Enter the desired number of queens:")
N = int(input())

# Generate a chessboard with dimensions N x N with all indexes set to 0.
board = [[0]*N for _ in range(N)]

# Keep track of how many valid nodes are generated.
nodeCount = 0

# Function to determine if a given index is valid for queen placement.
def isPromising(i, j):

    '''
    Check if there is an attacking queen in a given index's
    column and row.
    '''
    for k in range(0, N):

        # Return 'True' if there is an attacking queen
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    '''
    Check if there is an attacking queen in a given index's
    intersecting diagonals.
    '''
    for k in range(0, N):
        for l in range(0, N):

            # If a given k,l index is diagonal to a given i,j index...
            if (k + l == i + j) or (k - l == i - j):
    
                # Return 'True' if there is an attacking queen
                if board[k][l] == 1:
                    return True

    # If there are no attacking queens, return 'False'
    return False

# Driver function for program
def nQueen(n, ncount):

    # Once all queens have been placed, print # of nodes generated
    if n == 0:
        print("Solution nodes generated: ", ncount)
        return True

    for i in range(0, N):
        for j in range(0, N):

            '''
            If there isn't an attacking queen and the current index is
            empty, place a queen.
            '''
            if (not(isPromising(i, j))) and (board[i][j] != 1):
                
                # Place queen
                board[i][j] = 1

                # Increment number of solutions by 1
                ncount += 1

                '''
                Recursively call the function, attempt to place another
                queen given the updated chessboard.
                '''
                if nQueen(n-1, ncount+1) == True:
                    return True

                '''
                If placing a queen on the board doesn't lead to a solution,
                remove the queen.
                '''
                board[i][j] = 0

    # If a queen cannot be placed anywhere on the board, return 'False'
    return False

# Call driver function
nQueen(N, nodeCount)

# Print completed chessboard
print("Completed board:")
for i in board:
    print (i)