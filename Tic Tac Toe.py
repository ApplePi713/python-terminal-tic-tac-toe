import random

def run1(board,chosen):
  if (board[1] == 'O' and board[2] == 'O' and board[0] != 'X') or (board[3] == 'O' and board[6] == 'O' and board[0] != 'X') or (board[4] == 'O' and board[8] == 'O' and board[0] != 'X'):
    if 1 not in chosen:
      choice = 1
      return choice
  elif (board[0] == 'O' and board[2] == 'O'and board[1] != 'X') or (board[4] == 'O' and board[7] == 'O'and board[1] != 'X'):
    if 2 not in chosen:
      choice = 2
      return choice
  elif (board[0] == 'O' and board[1] == 'O' and board[2] != 'X') or (board[5] == 'O' and board[8] == 'O' and board[2] != 'X') or (board[4] == 'O' and board[6] == 'O' and board[2] != 'X'):
    if 3 not in chosen:
      choice = 3
      return choice
  elif (board[0] == 'O' and board[6] == 'O' and board[3] != 'X') or (board[4] == 'O' and board[5] == 'O' and board[3] != 'X'):
    if 4 not in chosen:
      choice = 4
      return choice
  elif (board[1] == 'O' and board[7] == 'O' and board[4] != 'X') or (board[3] == 'O' and board[5] == 'O' and board[4] != 'X') or (board[0] == 'O' and board[8] == 'O' and board[4] != 'X') or (board[2] == 'O' and board[6] == 'O' and board[4] != 'X'):
    if 5 not in chosen:
      choice = 5
      return choice
  elif (board[2] == 'O' and board[8] == 'O' and board[5] != 'X') or (board[3] == 'O' and board[4] == 'O' and board[5] != 'X'):
    if 6 not in chosen:
      choice = 6
      return choice
  elif (board[7] == 'O' and board[8] == 'O' and board[6] != 'X') or (board[3] == 'O' and board[0] == 'O' and board[6] != 'X') or (board[4] == 'O' and board[2] == 'O' and board[6] != 'X'):
    if 7 not in chosen:
      choice = 7
      return choice
  elif (board[6] == 'O' and board[8] == 'O' and board[7] != 'X') or (board[1] == 'O' and board[4] == 'O' and board[7] != 'X'):
    if 8 not in chosen:
      choice = 8
      return choice
  elif (board[6] == 'O' and board[7] == 'O' and board[8] != 'X') or (board[2] == 'O' and board[5] == 'O' and board[8] != 'X') or (board[0] == 'O' and board[4] == 'O'):
    if 9 not in chosen:
      choice = 9
      return choice
  return False

def run2(board,chosen):
  if (board[1] == 'X' and board[2] == 'X' and board[0] != 'O') or (board[3] == 'X' and board[6] == 'X' and board[0] != 'O') or (board[4] == 'X' and board[8] == 'X' and board[0] != 'O'):
    if 1 not in chosen:
      choice = 1
      return choice
  elif (board[0] == 'X' and board[2] == 'X' and board[1] != 'O') or (board[4] == 'X' and board[7] == 'X'and board[1] != 'O'):
    if 2 not in chosen:
      choice = 2
      return choice
  elif (board[0] == 'X' and board[1] == 'X' and board[2] != 'O') or (board[5] == 'X' and board[8] == 'X' and board[2] != 'O') or (board[4] == 'X' and board[6] == 'X' and board[2] != 'O'):
    if 3 not in chosen:
      choice = 3
      return choice
  elif (board[0] == 'X' and board[6] == 'X' and board[3] != 'O') or (board[4] == 'X' and board[5] == 'X' and board[3] != 'O'):
    if 4 not in chosen:
      choice = 4
      return choice
  elif (board[1] == 'X' and board[7] == 'X' and board[4] != 'O') or (board[3] == 'X' and board[5] == 'X' and board[4] != 'O') or (board[0] == 'X' and board[8] == 'X' and board[4] != 'O') or (board[2] == 'X' and board[6] == 'X' and board[4] != 'O'):
    if 5 not in chosen:
      choice = 5
      return choice
  elif (board[2] == 'X' and board[8] == 'X' and board[5] != 'O') or (board[3] == 'X' and board[4] == 'X' and board[5] != 'O'):
    if 6 not in chosen:
      choice = 6
      return choice
  elif (board[7] == 'X' and board[8] == 'X' and board[6] != 'O') or (board[3] == 'X' and board[0] == 'X' and board[6] != 'O') or (board[4] == 'X' and board[2] == 'X' and board[6] != 'O'):
    if 7 not in chosen:
      choice = 7
      return choice
  elif (board[6] == 'X' and board[8] == 'X' and board[7] != 'O') or (board[1] == 'X' and board[4] == 'X' and board[7] != 'O'):
    if 8 not in chosen:
      choice = 8
      return choice
  elif (board[6] == 'X' and board[7] == 'X' and board[8] != 'O') or (board[2] == 'X' and board[5] == 'X' and board[8] != 'O') or (board[0] == 'X' and board[4] == 'X' and board[8] != 'O'):
    if 9 not in chosen:
      choice = 9
      return choice
  return False
  
def almostwin(board,chosen,playernum):
  if playernum == 1:
    choice = run1(board,chosen)
    if choice == False:
      choice = run2(board,chosen)
      return choice
    else:
      return choice
  elif playernum == 2:
    choice = run2(board,chosen)
    if choice == False:
      choice = run1(board,chosen)
      return choice
    else:
      return choice
  
def computer(playernum,chosen,board,difficulty):
  print("The computer is making a move.")
  if len(chosen) < 9:
    if difficulty == 'e':
      choice = random.randint(1,9)
      if choice in chosen:
        while choice in chosen:
          choice = random.randint(1,9)
      if playernum == 1:
        board[choice-1] = 'O'
      elif playernum == 2:
        board[choice-1] = 'X'
      chosen.append(choice)
    else:
      if playernum == 2 and len(chosen)==0:
        choice = random.choice([1,3,7,9])
        board[choice-1] = 'X'
        chosen.append(choice)
      elif playernum == 1 and len(chosen)==1 and 5 not in chosen:
        choice = 5
        board[choice-1] = 'O'
        chosen.append(choice)
      elif almostwin(board,chosen,playernum) == False:
        if len(chosen) == 0:
          choice = 5
          if playernum == 1:
            board[choice-1] = 'O'
          elif playernum == 2:
           board[choice-1] = 'X'
          chosen.append(choice)
        else:
          choice = chosen[len(chosen)-1]
          if choice == 1:
            choice = 9
          elif choice == 2:
            choice = 8
          elif choice == 3:
            choice = 7
          elif choice == 4:
            choice = 6
          elif choice == 6:
            choice = 4
          elif choice == 7:
            choice = 3
          elif choice == 8:
            choice = 2
          elif choice == 9:
            choice = 1
          elif choice == 5:
            choice = random.randint(1,9)
          if choice in chosen:
            while choice in chosen:
              choice = random.randint(1,9)
          if playernum == 1:
            board[choice-1] = 'O'
          elif playernum == 2:
            board[choice-1] = 'X'
          chosen.append(choice)
      else:
        choice = almostwin(board,chosen,playernum)
        if playernum == 1:
          board[choice-1] = 'O'
        elif playernum == 2:
          board[choice-1] = 'X'
        chosen.append(choice)


def showboard(board):
  print(board[0], board[1], board[2])
  print(board[3], board[4], board[5])
  print(board[6], board[7], board[8])

def play(playernum,turn,chosen,board,difficulty):
  if len(chosen) < 9:
    if turn == 0 and playernum == 1:
      choice = input("Which space would you like to choose? 1-9: ")
      if choice in ['1','2','3','4','5','6','7','8','9',1,2,3,4,5,6,7,8,9]:
        choice = int(choice)
      if choice not in chosen and choice in range(1,10):
        board[choice-1] = 'X'
        chosen.append(choice)
        showboard(board)
        return True
      else:
        print("You can't choose there.")
        return False
    elif turn == 1 and playernum == 2:
      choice = int(input("Which space would you like to choose? 1-9: "))
      if choice not in chosen and choice in range(1,10):
        board[choice-1] = 'O'
        chosen.append(choice)
        showboard(board)
        return True
      else:
        print("You can't choose there.")
        return False
    else:
      computer(playernum,chosen,board,difficulty)
      showboard(board)
      return True

def tictactoe():
  turn = 0
  board = [1,2,3,4,5,6,7,8,9]
  chosen = []

  print("The board is laid out like so:")
  print("1 2 3")
  print("4 5 6")
  print("7 8 9")

  playernum = input("Do you want to be player 1 or player 2? Enter a number: ")
  if playernum not in ['1','2',1,2]:
    while playernum not in ['1','2',1,2]:
      print("You can't be that player. Please try again.")
      playernum = int(input("Do you want to be player 1 or player 2? Enter a number: "))
  if playernum == '1':
    playernum = 1
    print("You are X's.")
  if playernum == '2':
    playernum = 2
    print("You are O's")

  difficulty = input("What would you like the difficulty level to be? Easy or hard: ")
  if difficulty not in ["easy","Easy","EASY","e","E","hard","Hard","HARD","h","H"]:
    while difficulty not in ["easy","Easy","EASY","e","E","hard","Hard","HARD","h","H"]:
      print("That's not a difficulty level option.")
      difficulty = input("What would you like the difficulty level to be? Easy or hard: ")
  if difficulty in ["easy","Easy","EASY","e","E"]:
    difficulty = 'e'
  else:
    difficulty = 'h'

  while len(chosen) <= 9:
    if play(playernum,turn,chosen,board,difficulty) == False:
      while play(playernum,turn,chosen,board,difficulty) == False:
        play(playernum,turn,chosen,board,difficulty)
    turn = (turn + 1)%2

    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
      if playernum == 1:
        print("Wow! You won!")
        break
      else:
        print("Ahh. You lost.")
        break
    elif (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
      if playernum == 2:
        print("Wow! You won!")
        break
      else:
        print("Ahh. You lost.")
        break
    elif len(chosen) == 9:
      print("It's a tie!")
      break
  
  response = input("Do you want to play again? Yes or no: ")

  if response not in ["yes","YES","Yes","Y","y","no","NO","No","N","n"]:
    while response not in ["yes","YES","Yes","Y","y","no","NO","No","N","n"]:
      print("I'm sorry, but I don't understand that.")
      response = input("Do you want to play again? Yes or no: ")
  elif response in ["yes","YES","Yes","Y","y"]:
    print("\033c")
    tictactoe()
  elif response in ["no","NO","No","N","n"]:
    print("Goodbye!")

tictactoe()