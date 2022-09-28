import math
INT_MAX = math.inf
INT_MIN = -math.inf
ai,human='X','O'
import time

"""Declaring important global variables and importing few useful libraries"""

def check_ifPlayerWon(matrix,player):        
  if(matrix[0][0]==player and matrix[0][1]==player and matrix[0][2]==player):  # row 1 check
    return True
  elif(matrix[1][0]==player and matrix[1][1]==player and matrix[1][2]==player): # row 2 check
    return True
  elif(matrix[2][0]==player and matrix[2][1]==player and matrix[2][2]==player): # row 3 check
    return True
  elif(matrix[0][0]==player and matrix[1][0]==player and matrix[2][0]==player): # col 1 check
    return True
  elif(matrix[0][1]==player and matrix[1][1]==player and matrix[2][1]==player): # col 2 check 
    return True
  elif(matrix[0][2]==player and matrix[1][2]==player and matrix[2][2]==player): # col 3 check
    return True
  elif(matrix[0][0]==player and matrix[1][1]==player and matrix[2][2]==player): # diagnol 1 check
    return True
  elif(matrix[2][0]==player and matrix[1][1]==player and matrix[0][2]==player): # diagnol 2 check
    return True
  return False


def utility_value(matrix):
  if(check_ifPlayerWon(matrix,'X')==True):
    return 1
  if(check_ifPlayerWon(matrix,'O')==True):
    return -1
  return 0

def isFilled_board(matrix):
  for i in range(3):
    for j in range(3):
      if matrix[i][j]=='.':
        return False
  return True



def computer_move(board):              # computer move is made by recursively checking all available positions in board and choses the move which has the highest minimax value
  bestval=INT_MIN
  bestmove=()
  for i in range(3):
    for j in range(3):
      if(board[i][j]=='.'):
        board[i][j]=ai
        val=minimax(board,False)
        board[i][j]='.'
        if(val > bestval):
          bestval=val
          bestmove=(i,j)
  board[bestmove[0]][bestmove[1]]=ai



def minimax(board,isMax):
  if(isFilled_board(board)):                    # return the utility value of board if the board is filled
    return utility_value(board)

  if(check_ifPlayerWon(board,human) or check_ifPlayerWon(board,ai)):    # return the utility value according to either ai or human won
    return utility_value(board)
  
  if(isMax==True):
    bestVal=INT_MIN
    for i in range(3):
      for j in range(3):
        if(board[i][j]=='.'):
          board[i][j]=ai
          val=minimax(board,False)
          bestVal=max(val,bestVal)
          board[i][j]='.'
    return bestVal

  else:
    bestVal=INT_MAX
    for i in range(3):
      for j in range(3):
        if(board[i][j]=='.'):
          board[i][j]=human
          val=minimax(board,True)
          bestVal=min(val,bestVal)
          board[i][j]='.'
    return bestVal



def print_board(matrix):                       # for clean display of board configuration
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      print(matrix[i][j],"  |  ",end="")
    print()
  print("===============================")



def Start_Game():
  board=[['.','.','.'],['.','.','.'],['.','.','.']]    # inital config of board 
  start=time.process_time()
  while(isFilled_board(board)==False):      # Runs loop until game is finished or board is filled
    print("Computer move")
    computer_move(board)              # First Move is made by computer
    print_board(board)
    if(check_ifPlayerWon(board,ai)):
      print("Computer Won")
      break
    if(isFilled_board(board)):
      print("Tie")
      break
    print("User move")
    print("Enter the Move (row,column):")
    user_move=list(map(int,input().split()))
    board[user_move[0]][user_move[1]]='O'
    print_board(board)
    if(check_ifPlayerWon(board,human)):
      print("User won")
      break
  end=time.process_time()
  print("=================")
  print("Time taken is :",end-start,"sec")


if __name__=="__main__":
  Start_Game()