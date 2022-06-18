# %% 
# I consider that the body is the snake without include the head (1st position of the array)
# and the tail (last position of the array)
# Return true is pos is part of the snake body
def isSnakeBody(pos, snake):
    return pos in snake[1:-1]

# Check that it is not out of board 
def isOutOfBoard(pos, board):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= board[0] or pos[1] >= board[1]


# Check if the snake is well builted 
def isSnakeGood(board, snake):
    result = True
    i = 0

    while(i+1 < len(snake) and result):
        print(i)
        # Position out of board
        if snake[i] == -1:
            result = False
        # Take pair
        auxSnake = [snake[i], snake[i+1]]
        havePairNear = False
        for j in range(4):
            # Move to all near position 
            prove = movePosition(board, auxSnake, snake[i], j)
            # Head is trying to move to the tails position so its near
            if prove[0] == -3:
                havePairNear = True
        if not havePairNear:
            print(snake[i])
            result = False
        i+=1
    return result
  
  
def movePosition(board, snake, pos, movement):
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

    if isOutOfBoard(newPosition,board):
        newPosition = [-1]       
    # The head eat the body 
    if newPosition[0] != -1 and isSnakeBody(newPosition,snake):
        newPosition = [-2]
    # The snake only have head and tail and the head is moving to the tail position
    if len(snake) == 2 and (newPosition == snake[-1]):
        newPosition = [-3]
        
    return newPosition


def numberOfAvailableDifferentPaths(board, snake, depth):
    result = 1
    if depth != 0:
        for j in range(4):
            newPosition = movePosition(board,snake,snake[0],j)
            # If there is not errors we move all the snake
            if newPosition[0] >= 0 :
                print("----------")
                print("Depth: "+ str(depth))
                # Delete last position (tail position now is the penultim position)
                # and add the new position (new tail) as first 
                newSnake = [newPosition, *snake[:-1]]
                print("Move "+ str(j),end="")
                print(newSnake)
                printBoardWithSnake(board,newSnake)
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

goodSnake = list(map(lambda x: [x[1],x[0]] ,snake))
goodBoard = [3,4]
depth = 3
print("Initial snake positions: ")
print(goodSnake)
print("Initial board: ")
printBoardWithSnake(goodBoard,goodSnake)
print(numberOfAvailableDifferentPaths(goodBoard,goodSnake,depth))
# print(isSnakeGood(board,goodSnake[:2]))


# %% 



# %%
