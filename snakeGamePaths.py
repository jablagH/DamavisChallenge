# %% 

def isSnakeBody(pos, snake):
    """
    I consider that the body is the snake's cells without include the head (1st position of the array)
    and the tail (last position of the array). Return if pos is part of the snake body.

    Args:
        snake (list.list.integer): snakes cells cordinates
        pos (list.integer): coordinates of the position to check

    Returns:
        True : if pos is part of the snake body
        False: if pos is not part of the snake body
    """
    return pos in snake[1:-1]

# Check if a position it is not out of board 
def isOutOfBoard(pos, board):
    """
    Check if a position it is not out of board 

    Args:
        board (list.integer): board dimensions
        pos (list.integer): coordinates of the position to check

    Returns:
        True : if pos is out of the board dimensions
        False: if pos is not out of the board dimensions
    """
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= board[0] or pos[1] >= board[1]

 
def isSnakeGood(board, snake):
    """   
    Check if the snake cells are well builted, the snake has one or more cells such those
    cells are horizontally or vertically adjacent and are inside the board dimensions.
    
    Args:
        board (list.integer): board dimensions
        snake (list.list.integer): snakes cells cordinates

    Returns:
        True : if the snake cells are well builted
        False: if the snake cells are not well builted
    """

    result = True
    i = 0

    while(i+1 < len(snake) and result):
        print(i)
        # Position out of board
        if snake[i] == -1:
            result = False
        # Take pair
        pairOfSnakeCells = [snake[i], snake[i+1]]
        havePairNear = False
        for j in range(4):
            # Move to all adjacent position 
            prove = movePosition(board, pairOfSnakeCells, snake[i], j)
            # Head is trying to move to the tail's position so the pair of cells are adjacent.
            if prove[0] == -3:
                havePairNear = True
        if not havePairNear:
            print(snake[i])
            result = False
        i+=1
    return result


def movePosition(board, snake, pos, movement):
    """            
    Due a position (pos), a board dimensions (board) and a array with the positions 
    of the snake's cells (snake) try to move to:

    Args:
        board (list.integer): board dimensions
        snake (list.list.integer): snakes cells cordinates
        pos (list.integer): inital position
        movement (_type_): Number between 0 and 4, is want to move to:
            - The right cell set it to 0
            - The left cell set it to 1
            - The up cell set it to 2
            - The down cell set it to 3

    Returns:
        [i,j] : Where [i,j] are the coordinates in the board if we can move to that position
        [-1]  : If the position where we are trying to move is out of board
        [-2]  : If the position where we are trying to move is part of the snake body
        [-3]  : If the snake only have head and tail (len(snake)=2) and the head is trying to move to the tail position
    
    """
    moveRow = -1
    moveColum = -1
    # Move rigth
    if(movement == 0):
        moveRow = pos[0]
        moveColum = pos[1] + 1
    # Move left
    elif(movement == 1): 
        moveRow = pos[0]
        moveColum = pos[1] -1
    # Move down
    elif(movement == 2): 
        moveRow = pos[0] + 1
        moveColum = pos[1]
    # Move up
    elif(movement == 3): 
        moveRow = pos[0] - 1
        moveColum = pos[1] 
    
    newPosition = [moveRow, moveColum]
    # The cell where you wanna go is out of board
    if isOutOfBoard(newPosition,board):
        newPosition = [-1]       
    # The head eat the body 
    if newPosition[0] != -1 and isSnakeBody(newPosition,snake):
        newPosition = [-2]
    # The snake only have head and tail (snake.lenght=2) and the head is moving to the tail position
    if len(snake) == 2 and (newPosition == snake[-1]):
        newPosition = [-3]
        
    return newPosition


def numberOfAvailableDifferentPaths(board, snake, depth):
    result = 0
    if depth != 0:

        for j in range(4):
            newPosition = movePosition(board,snake,snake[0],j)
            # If there is not errors we move all the snake cells
            if newPosition[0] >= 0 :

                # Delete last position (tail position now has previous penultim position)
                # and add the new position (new head) as first 
                newSnake = [newPosition, *snake[:-1]]
                
                # Lines to print the snake on the board and debug
                print("----------")
                numMoveToLetter  = {0:'R', 1:'L', 2:'D', 3:'U'}
                print("Depth: "+ str(depth))
                print("Move "+ numMoveToLetter.get(j)+" snake new position: ",end="")
                print(newSnake)
                printBoardWithSnake(board,newSnake)
                
                if depth == 1:
                    result += 1
                else:
                    result += numberOfAvailableDifferentPaths(board,newSnake,depth-1)

    return result


def printBoardWithSnake(board, snake):
    for i in range(board[0]):
        for j in range(board[1]):
            if [i,j] in snake:
                print(str(snake.index([i,j]))+" ",end="")

            else:
                print("+ ",end="") 
        print()
            
# To do 
#   - Calculate the number of available different Paths
#   - Check inicial inputs values

    
board = [4, 3]
snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3
print("Initial snake positions: ")
print(snake)
print("Initial board: ")
printBoardWithSnake(board,snake)
print(numberOfAvailableDifferentPaths(board,snake,depth))
# print(isSnakeGood(board,goodSnake[:2]))
# %% 
aux  = {0:'R', 1:'L', 2:'D', 3:'U'}
print(aux.get(0))
# %%
