game = [["*","*","*"],["*","*","*"],["*","*","*"]]

#Creating the Boards
def drawBoard():
  #3x3 Board
  for i in range(3):
    print("---".join("    "))
    for j in range(3):
      print("| "+game[i][j], end=" ")
    print("|")
  print("---".join("    "))

#Setting Player Scores
p1Score = 0
p2Score = 0
def printScore():
  #p1Score = p1Score+1
  global p1Score, p2Score
  #global p1Score
  #global p2Score
  print("Player 1 Score:", p1Score)
  print("Player 2 Score:", p2Score)

def checkWinRowCol():
  global game, p1Score, p2Score
  for row1 in range(2):
    if (game[row1][0] == game[row1][1] == game[row1][2] == "X"):
      print("Player 1 wins!")
      p1Score +=1
      return True
  for col1 in range(2):
    if (game[0][col1] == game[1][col1] == game[2][col1] == "X"):
      print("Player 1 wins!")
      p1Score +=1
      return True
  for row2 in range(2):
    if (game[row2][0] == game[row2][1] == game[row2][2] == "X"):  
      print("Player 2 wins!")
      p2Score +=1
      return True
    for col2 in range(2):
      if (game[0][col2] == game[1][col2] == game[2][col2] == "X"):
        print("Player 2 wins!")
        p2Score +=1
        return True
  return False

def checkDiag():
  global game, p1Score, p2Score
  if ((game[0][0] == game[1][1] == game[2][2] and game[0][0] == "X") or
  (game[0][2] == game[1][1] == game[2][0] and game[0][2] == "X")): 
    print("Player 1 Wins!")
    p1Score += 1
    return True
  elif ((game[0][0] == game[1][1] == game[2][2] and game[0][0] == "O") or
  (game[0][2] == game[1][1] == game[2][0] and game[0][2] == "O")): 
    print("Player 2 Wins!")
    p2Score += 1
    return True
  else:
    return False

def playGame():
  global game
  x = 0
  while (x < 9):
    p1row = int(input("Player 1 enter row: "))
    while (p1row < 1 or p1row > 3):
      print("Input invalid. Please try again: ")
      p1row = int(input("Player 1 enter row: "))
    p1col = int(input("Player 1 enter column: "))
    while (p1col < 1 or p1col > 3):
      print("Input invalid. Please try again: ")
      p1col = int(input("Player 1 enter column: "))
    if (game[p1row-1][p1col-1] == "*"):
      game[p1row-1][p1col-1] = "X"
    drawBoard()
    if (checkDiag() or checkWinRowCol()):
      resetGame()
      break
    else:
      x += 1
    p2row = int(input("Player 2 enter row: "))
    while (p2row < 1 or p2row > 3):
      print("Input invalid. Please try again: ")
      p2row = int(input("Player 2 enter row: "))
    p2col = int(input("Player 2 enter column: "))
    while (p2col < 1 or p2col > 3):
      print("Input invalid. Please try again: ")
      p2col = int(input("Player 2 enter column: "))
    if (game[p2row-1][p2col-1] == "*"):
      game[p2row-1][p2col-1] = "O"
    drawBoard()
    if (checkDiag() or checkWinRowCol()):
      resetGame()
      break
    else:
      x += 1
    if (x >= 8):
      print("Players have tied.")
      break

def userWantsToQuit():
  quit = input("Enter q to quit or any other char to continue: ")
  if (quit=="q"):
    return True
  else:
    return False

#setting game board back to initial
def resetGame():
  global game
  game = [["*","*","*"],["*","*","*"],["*","*","*"]]

print("Welcome to Tic Tac Toe!")
print("1. Single Game")
print("2. Unlimited Play")
print("3. Up to 5 Wins")
#Getting User Input for Style of Play
choice = input("Please enter a number from 1-3: ")
if (choice == "1"):
  print("You have chosen single game!")
  while True:
    drawBoard()
    playGame()
elif (choice=="2"):
  print("You have chosen unlimited play!")
  while (True):
    for l in range(1):
      drawBoard()
      playGame()
      printScore()
      resetGame()
      if (userWantsToQuit()):
        break
elif (choice=="3"):
  print("You have chosen up to 5 Wins")
  h = int(input("Please enter a number from 0-4: "))
  for h in range (5):
    while (p1Score < h or p2Score < h):
      drawBoard()
      playGame()
      printScore()
      resetGame()
      if (p1Score == h or p2Score == h):
        print("Thank you for playing!")
        break    
  else:
    print("Input invalid. Please try again.")
else:
  print("Input invalid. Please try again.")


