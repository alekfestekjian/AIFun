import random
import string
def drawBoard(board):
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('------------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('------------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def inputPlayerLetter():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O?')
		letter = raw_input().upper()
	if letter == 'X':
		return ['X','O']
	else:
		return ['O','X']

def playAgain():
	return raw_input('Do you want to play again? (y/n)').lower().startswith('y')

def makeMove(board, letter, move):
	board[move] = letter

def whoGoesFirst():
	counter = random.random()
	if counter < .5:
		print 'computer'
	else:
		print 'player'
#board = b
#letter = l
def isWinner(b, l):
	if (b[7] == l and b[8] == l and b[9] == l):
		return True
	elif (b[4] == l and b[5] == l and b[6] == l):
		return True
	elif (b[1] == l and b[2] == l and b[3] == l):
		return True
	elif (b[7] == l and b[4] == l and b[1] == l):
		return True
	elif (b[8] == l and b[5] == l and b[2] == l):
		return True
	elif (b[9] == l and b[6] == l and b[3] == l):
		return True
	elif (b[7] == l and b[5] == l and b[3] == l):
		return True
	elif (b[9] == l and b[5] == l and b[1] == l):
		return True


def getBoardCopy(board):
	copyBoard = []
	for i in board:
		copyBoard.append(i)

	return copyBoard
def isSpaceFree(board, move):
	if board[move] == ' ':
		return True
	else:
		return false

def getPlayerMove(board):
	#move = ' '
	playerMove = raw_input('What is your next move? (1-9)')
	while int(playerMove) not in range(1,10) or not isSpaceFree(board, int(playerMove)):
		move = raw_input('What is your next move? (1-9)')
	return int(playerMove)
def chooseRandomMoveFromList(board, movesList):
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None
#FINISH this function
def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'
	#checks if computer can win next turn
	for i in range(1,10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i
	for i in range(1,10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i
	#take center
	if isSpaceFree(board,5):
		return 5
	#take one of the corners
	if chooseRandomMoveFromList(board, [1,3,7,9]) != None:
		return move
	#take one of the sides
	return chooseRandomMoveFromList(board, [2,4,6,8])

def isBoardFull(board):
	for i in range(1,10):
		if isSpaceFree(board, i):
			return False
	return True

print('Try your best to beat me! ')

while True:
	theBoard = [' '] * 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print(turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			print "Hi"

	if not playAgain():
		break	
