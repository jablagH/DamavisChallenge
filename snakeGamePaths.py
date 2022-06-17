# I consider that the body is the snake without include the head (1st position of the array)
# and the tail (last position of the array)
# Return true is pos is part of the snake body
def isSnakeBody(pos, snake):
    return pos in snake[1:-1]


# If we can move the head to the right it returns the new head position
# If we cannot move the head to the right return empty list
def moveHeadRight(board, snake):
    headPosition = snake[0]  
    moveRow = headPosition[0]
    moveColum = headPosition[1] + 1
    newMovement = [moveRow, moveColum]
    # Check that it is not out of bounds and is not a part of the body
    if moveColum > (board[1] - 1) or isSnakeBody(newMovement,snake):
        newMovement = []
    return newMovement

# If we can move the head to the left it returns the new head position
# If we cannot move the head to the left return empty list
def moveHeadLeft(snake):
    headPosition = snake[0]
    moveRow = headPosition[0]
    moveColum = headPosition[1] - 1
    newMovement = [moveRow, moveColum]
    # Check that it is not out of bounds and is not a part of the body
    if moveColum < 0 or isSnakeBody(newMovement,snake):
        newMovement = []
        
    return newMovement

# If we can move the head down it returns the new head position
# If we cannot move the head down return empty list
def moveHeadDown(board,snake):
    headPosition = snake[0]
    moveRow = headPosition[0] + 1
    moveColum = headPosition[1]
    newMovement = [moveRow, moveColum]
    # Check that it is not out of bounds and is not a part of the body
    if moveRow > (board[0] - 1) or isSnakeBody(newMovement,snake):
        newMovement = []
    return newMovement
    
# If we can move the head up it returns the new head position
# If we cannot move the head up return empty list
def moveHeadUp(snake):
    newMovement = []
    headPosition = snake[0]
    moveRow = headPosition[0] - 1
    moveColum = headPosition[1]
    newMovement = [moveRow, moveColum]
    # Check that it is not out of bounds and is not a part of the body
    if moveRow < 0 or isSnakeBody(newMovement,snake):
        newMovement = [] 
    return newMovement

def numberOfAvailableDifferentPaths(board, snake, depth):
    return 0

               
def moveBody():
    return

# To do 
#   - Guaranteed that snake[i] and snake[i + 1] are horizontally or vertically adjacent, and that its initial configuration is valid
#   - Calculate the number of available different Paths

board = [4, 3]
snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3

print(snake[0])
print("Right: ", end='')
print(moveHeadRight(board,snake))

print("Left: ", end='')
print(moveHeadLeft(snake))

print("Up: ", end='')
print(moveHeadUp(snake))

print("Down: ", end='')
print(moveHeadDown(board,snake))

    



