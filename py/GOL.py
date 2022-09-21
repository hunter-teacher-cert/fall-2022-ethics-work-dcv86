# FILENAME
# Dave Ciolino-Volano
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: Christine Marra

import time
import os
import random

class Cgol :

	
	def  createNewBoard( rows,  cols) :
		board = [[' '] * (cols) for _ in range(rows)]
		i = 0
		while (i < rows) :
			j = 0
			while (j < cols) :
				board[i][j] = ' '
				j += 1
			i += 1
		return board
	# print the board to the terminal
	#@staticmethod
	def printBoard(board) :
		j = 0
		while (j < len(board[0]) + 2) :
			print('-', end ="")
			j += 1
		print()
		i = 0
		while (i < len(board)) :
			print('|', end ="")
			j = 0
			while (j < len(board[i])) :
				print(board[i][j], end ="")
				j += 1
			# System.out.print('\n');
			print('|')
			i += 1
		j = 0
		while (j < len(board[0]) + 2) :
			print('-', end ="")
			j += 1
		print()
	# set cell (r,c) to val
	
	def setCell( board,  r,  c,  val) :
		board[r][c] = val
	# return number of living neigbours of board[r][c]
	def  countNeighbours( board,  r,  c) :
		num = 0
		# countNeighbors  X = alive space i= dead
		i = r - 1
		while (i <= r + 1) :
			j = c - 1
			while (j <= c + 1) :
				if ((i >= 0 and i < len(board) and j >= 0 and j < len(board[0])) and (i != r or j != c)) :
					# *look at squares around* make sure its not focused on center squre
					if (board[i][j] == 'X') :
						num += 1
				j += 1
			i += 1
		return num
	# *
	#	 precond: given a board and a cell
	#	 postcond: return next generation cell state based on CGOL rules
	#	 (alive 'X', dead ' ')
	def  getNextGenCell(board,  r,  c) :
		myCell = 'X'
		numLiveNeigh = Cgol.countNeighbours(board, r, c)
		# System.out.println("Row "+r+" Column "+c+ " NC "+numLiveNeigh);
		# in.nextLine();
		if (board[r][c] == 'X') :
			if (numLiveNeigh < 2 or numLiveNeigh > 3) :
				myCell = ' '
		elif(board[r][c] == ' ') :
			if (numLiveNeigh != 3) :
				myCell = ' '
		return myCell
	# generate and return a new board representing next generation

	def  generateNextBoard(board) :
		nextBoard = [[' '] * (len(board[0])) for _ in range(len(board))]
		i = 0
		while (i < len(board)) :
			j = 0
			while (j < len(board[i])) :
				Cgol.setCell(nextBoard, i, j, Cgol.getNextGenCell(board, i, j))
				j += 1
			i += 1
		return nextBoard

	def main( args) :
		#	*  Same as
		#	*  char[][] test;
		#	*  char[][] lastGen;
		test = None
		lastGen = None
		test = Cgol.createNewBoard(25, 25)
		# imbueLife(test,200);
		Cgol.setCell(test, 0, 0, 'X')
		Cgol.setCell(test, 0, 1, 'X')
		Cgol.setCell(test, 1, 0, 'X')
		i = 0
		while (i < 5) :
			print("Generation " + str(i))
			Cgol.printBoard(test)
			input()
			# it won't continue the program until the user presses the 'enter' key
			test = Cgol.generateNextBoard(test)
			i += 1
	

if __name__=="__main__":
	Cgol.main([])
