"""
Make sure to fill in the following information before submitting your
assignment. Your grade may be affected if you leave it blank!
For usernames, make sure to use your Whitman usernames (i.e. exleyas). 
File name: minesweeper9000.py
Author username(s): mcclelnr
Date: December 12th, 2017

Game: Minesweeper 9000
Description: it is an adaptation of the classic 1989 game Minesweeper. I do not take credit
for the concept of this game nor the graphics module that is used to play it (graphics.py).
"""
import graphics
import random
import time

class button:
	'''Used to determine the cell that was clicked'''
	def wasClicked(point, cell_list, width):
		"""Returns the cell clicked
			Parameters:
				point: The point that a user clicked
				cell_list: list of cells to search through
				width: width of each cell
		"""
		for cell in cell_list: #iterates through the list of cells
			if ((cell[0] - width) <= point[0] <= (cell[0] + width)) \
			and ((cell[1] - width) <= point[1] <= (cell[1] + width)):
				return cell #returns if the point clicked is in the cell

class background:
	'''Used to set the window background'''
	def set_background(win):
		'''Colors the window background
		Parameters:
			win: the window to draw to
		'''
		win.setBackground('grey') #sets background color to grey

		board = graphics.Rectangle(graphics.Point(10,10), graphics.Point(690,690))
		board.setFill('white')
		board.draw(win) #draws a white rectangle to be the board

	def create_board(win, difficulty, celllist):
		'''Draws the game board
		Parameters:
			difficulty: is 1/10th the width and height of each cell
			win: the window to draw to
		'''
		color_list = ['pink', 'orange', 'yellow', 'light green', 'light blue', 'purple', 'white']

		#grid_outline is a list lines that outline the game board
		grid_outline = [graphics.Line(graphics.Point(10,10),graphics.Point(10,690)),
		graphics.Line(graphics.Point(10,10),graphics.Point(690,10)),
		graphics.Line(graphics.Point(10,690),graphics.Point(690,690)),
		graphics.Line(graphics.Point(690,10),graphics.Point(690,690))]

		for line in grid_outline: #iterates over every outline and draws it
				line.draw(win)

		colorful_board = False
		if difficulty > 4: #if there aren't too many cells
			colorful_board = background.ask_colorful(win)
		if colorful_board == True:
			color = 0
			for cell in celllist:
				colored_cell = graphics.Rectangle(graphics.Point(cell[0] - 5 * \
					difficulty, cell[1] + 5 *difficulty), \
					graphics.Point(cell[0] + 5 * difficulty, cell[1] - 5 * difficulty))
				colored_cell.setFill(color_list[color % 7])
				colored_cell.draw(win)
				color += 1
		else: #otherwise don't make the cells colorful
			#iterates over the number of grid lines to be drawn for 
				#that difficulty and draws them
			for line in range(680 // int(10 * difficulty)):
				graphics.Line(graphics.Point((10 + (difficulty  * 10) * line), 10), \
					graphics.Point((10 + (difficulty  * 10) * line), 690)).draw(win)
				graphics.Line(graphics.Point(10, (10 + (difficulty  * 10) * line)), \
					graphics.Point(690, (10 + (difficulty  * 10) * line))).draw(win)

	def ask_colorful(win):
		'''Asks the user if they want to play again and returns 'yes' or 'No'
		Parameters:
			win: the window to draw to
		'''
		#creates a rectangle that asks Play again? on the screen
		colorboard = graphics.Rectangle(graphics.Point(270, 250),\
			graphics.Point(430, 330))
		colorboard.setFill('light blue')
		tcolor = graphics.Text(graphics.Point(350, 290), "Colorful Board?")
		tcolor.setSize(18)
		tcolor.setFill('black')
		colorboard.draw(win)
		tcolor.draw(win)

		#creates another rect. that asks quit
		boring = graphics.Rectangle(graphics.Point(270, 380),\
			graphics.Point(430, 460))
		boring.setFill('grey')
		tboring = graphics.Text(graphics.Point(350, 420), "Plain Boring Board?")
		tboring.setSize(18)
		tboring.setFill('black')
		boring.draw(win)
		tboring.draw(win)

		#waits for user to click either Quit or Play again? and
			#returns the cooresponding value
		color = 'idk'

		while color == 'idk': 
			mouse = win.getMouse()
			if 270 < mouse.getX() < 430:
				if 250 < mouse.getY() < 330:
					color = True
				if 380 < mouse.getY() < 460:
					color = False
		
		colorboard.undraw()
		tcolor.undraw()
		boring.undraw()
		tboring.undraw()

		return color


class play_minesweeper_again:
	'''Used to ask the user if they want to play the game again'''
	def ask(win, already_drawn):
		'''Asks the user if they want to play again and returns 'yes' or 'No'
		Parameters:
			win: the window to draw to
		'''
		if already_drawn == 'no':
			#creates a rectangle that asks Play again? on the screen
			play_again = graphics.Rectangle(graphics.Point(230, 380),\
				graphics.Point(330, 460))
			play_again.setFill('grey')
			tplay = graphics.Text(graphics.Point(280, 420), "Play again?")
			tplay.setSize(18)
			tplay.setFill('black')
			play_again.draw(win)
			tplay.draw(win)

			#creates another rect. that asks quit
			quit = graphics.Rectangle(graphics.Point(370, 380),\
				graphics.Point(470, 460))
			quit.setFill('grey')
			tq = graphics.Text(graphics.Point(420, 420), "Quit")
			tq.setSize(18)
			tq.setFill('red')
			quit.draw(win)
			tq.draw(win)

		#waits for user to click either Quit or Play again? and
			#returns the cooresponding value
		play_again = 'idk'


		while play_again == 'idk': 
			mouse = win.getMouse()
			if 380 < mouse.getY() < 460:
				if 230 < mouse.getX() < 330:
					play_again = 'Yes'
				if 370 < mouse.getX() < 470:
					play_again = 'No'
			return play_again

class animations:
	'''A class of various animations used frequently'''
	def bombs(win, point, size):
		'''Draws a bomb
		Parameters:
			win: the window to draw to
			point: the point to draw the bomb to
		'''
		bomb = graphics.Circle(graphics.Point(point[0], point[1]), int(size))
		bomb.setFill('red')
		stem = graphics.Rectangle(graphics.Point(point[0], point[1]), \
			graphics.Point(point[0], point[1] - (size * 3/2)))
		stem.draw(win)
		bomb.draw(win)

	def flag(size, cell_to_flag):
		'''Draws a flag
		Parameters:
			size: the size of the flag to draw
			cell_to_flag: the cell that is to be flagged
		'''

		flag = graphics.Polygon(graphics.Point(cell_to_flag[0], cell_to_flag[1]), \
		 graphics.Point(cell_to_flag[0] + size, cell_to_flag[1]), \
		 graphics.Point(cell_to_flag[0], cell_to_flag[1] - size), \
		 graphics.Point(cell_to_flag[0], cell_to_flag[1] + size))
		flag.setFill('red')
		
		return flag

	def explosion(won, point, size, win, color = 'red'):
		'''Draws an explosion
		Parameters:
			won: if the player has won or not
			point: the point at which to draw the explosion
			size: the size of which to draw it
			win: the window to draw it
			color: the color explosion to draw, defaults to red
		'''
		explosion = graphics.Polygon(graphics.Point(point[0] + size * 2, point[1]), \
			graphics.Point(point[0] + size/2, point[1] + size/2), \
			graphics.Point(point[0], point[1] + size * 2), \
			graphics.Point(point[0] - size/2, point[1] + size/2), \
			graphics.Point(point[0] - size * 2, point[1]), \
			graphics.Point(point[0] - size/2, point[1] - size/2), \
			graphics.Point(point[0], point[1] - size * 2), \
			graphics.Point(point[0] + size/2, point[1] - size/2),)

		if won == True:
			explosion.setFill('yellow')
		else:
			explosion.setFill(color)

		explosion.draw(win)

class cell:
	'''Sets up the cells and difficulty of the game'''
	def cells(difficulty):
		'''is a list of lists with the coordinates for the center
		of each cell in it and returns it
		Parameters:
			difficulty: the type of board/ cell list to return
		'''
		if difficulty == 17:
			points = (95,265,435,605)
		elif difficulty == 6.8:
			points = (44,112,180,248,316,384,452,520,588,656)
		elif difficulty == 13.6:
			points = (78,214,350,486,622)
		elif difficulty == 4:
			points = (30,70,110,150,190,230,270,310,350,390,430,470,510,550,590,630,670)
		elif difficulty == 2:
			points = (20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,\
				320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,\
				620,640,660,680)
		elif difficulty == 1:
			points = (15,25,35,45,55,65,75,85,95,105,115,125,135,145,155,165,175,185,195,\
				205,215,225,235,245,255,265,275,285,295,305,315,325,335,345,355,365,375,385,395,\
				405,415,425,435,445,455,465,475,485,495,505,515,525,535,545,555,565,575,585,595,\
				605,615,625,635,645,655,665,675,685)

		cells = []

		#loop that appends cells with: an item in the list with everything else in the list
		for a in points: 
			for b in points:
				new_cell = (a,b)
				cells.append(new_cell)

		return cells

	def set_bombs(difficulty):
		'''Randomly sets bombs to coordinates in the coorisponding difficulty level
		and returns a list of the bomb cells
		Parameters:
			difficulty: used to determine the coorisponding amount of bombs to set
		'''
		bombcell = []
		if difficulty == 17:
			total_bombs = 0
			while total_bombs != 4:
				possible = (random.randrange(95,606,170), random.randrange(95,606,170))
				if possible == (95, 95):
					'do nothing'
				if possible not in bombcell:
					bombcell.append(possible)
					total_bombs += 1

		if difficulty == 6.8:
			total_bombs = 0
			while total_bombs != 20:
				possible = (random.randrange(44,656,68), random.randrange(44,656,68))
				if possible == (44,44):
					'do nothing'
				elif possible not in bombcell:
					bombcell.append(possible)
					total_bombs += 1

		if difficulty == 13.6:
			total_bombs = 0
			while total_bombs != 6:
				possible = (random.randrange(78,622,136), random.randrange(78,622,136))
				if possible == (78, 78):
					'do nothing'
				elif possible not in bombcell:
					bombcell.append(possible)
					total_bombs += 1

		if difficulty == 4:
			total_bombs = 0
			while total_bombs != 60:
				possible = (random.randrange(30,670,40), random.randrange(30,670,40))
				if possible == (30, 30):
					'do nothing'
				elif possible not in bombcell:
					bombcell.append(possible)
					total_bombs += 1

		if difficulty == 2:
			total_bombs = 0
			while total_bombs != 300:
				possible = (random.randrange(20,680,20), random.randrange(20,680,20))
				if possible == (20, 20):
					'do nothing'
				elif possible not in bombcell:
					bombcell.append(possible)
					total_bombs += 1

		if difficulty == 1:
			total_bombs = 0
			while total_bombs != 700:
				possible = (random.randrange(15,685,10), random.randrange(15,685,10))
				if possible == (15, 15):
					'do nothing'
				elif possible not in bombcell:
					bombcell.append(possible)
					total_bombs += 1

		return bombcell

	def get_nums(difficulty, celllist, bomblist):
		'''generates the amount of bombs around each cell
		and returns a dictionary containing each cell as the key
		and the key value as the amount of bombs around it
		Parameters:
			difficulty: to determine the neighbors around each cell
			celllist: the list of cells to gen numbers for
			bomblist: the list of bombs
		'''
		cell_num_dict = {}

		a = difficulty * 10

		neighbors = ((-a,a),(0,a),(a,a),(a,0),(a,-a),(0,-a),(-a,-a),(-a,0))
		#generates a list of neighbors cooresponding to the difficulty level

		for cell in celllist:
			if (cell[0], cell[1]) not in bomblist: #only iterates over non-bomb cells
				numb_bombs = 0 #initalizes number of bombs to zero
				for neigh in neighbors: #iterates over the list of neighboring cells
					if ((cell[0] + neigh[0]) > 10) and ((cell[0] + neigh[0]) < 690) \
					and ((cell[1] + neigh[1]) > 10) and ((cell[1] + neigh[1]) < 690):
						#asks if the neighboring cell is in the valid grid space
						for bomb in bomblist: #iterates over the list of bombs
							if int(cell[0] + neigh[0]) == bomb[0]\
							 and int(cell[1] + neigh[1]) == bomb[1]: 
							 #if the cell's neighbor equals a bomb
								numb_bombs += 1 #add another bomb to the amount
				cell_num_dict[(cell[0], cell[1])] = numb_bombs #add the cell as the key and
					#number of bombs as the key value to the dictionary
			else: #if it cell is a bomb
				cell_num_dict[(cell[0], cell[1])] = ''
				#add the cell as key and bomb as the key value to the dictionary

		return cell_num_dict

	def difficulty(win):
		'''Used to ask the user the desired difficulty/size of board
		and returns the cooresponding value
		Parameters:
			win: window to draw to
		'''
		#difficulty1
		difficulty1 = graphics.Rectangle(graphics.Point(150, 310),\
			graphics.Point(250, 390))
		difficulty1.setFill('black')
		tdif1 = graphics.Text(graphics.Point(200, 350), "4 Bombs")
		tdif1.setSize(18)
		tdif1.setFill('white')
		difficulty1.draw(win)
		tdif1.draw(win)

		#difficulty2
		difficulty2 = graphics.Rectangle(graphics.Point(300, 310),\
			graphics.Point(400, 390))
		difficulty2.setFill('black')
		tdif2 = graphics.Text(graphics.Point(350, 350), "6 Bombs")
		tdif2.setSize(18)
		tdif2.setFill('white')
		difficulty2.draw(win)
		tdif2.draw(win)

		#difficulty3
		difficulty3 = graphics.Rectangle(graphics.Point(450, 310),\
			graphics.Point(550, 390))
		difficulty3.setFill('black')
		tdif3 = graphics.Text(graphics.Point(500, 350), "20 Bombs")
		tdif3.setSize(18)
		tdif3.setFill('pink')
		difficulty3.draw(win)
		tdif3.draw(win)

		#difficulty4
		difficulty4 = graphics.Rectangle(graphics.Point(150, 410),\
			graphics.Point(250, 490))
		difficulty4.setFill('black')
		tdif4 = graphics.Text(graphics.Point(200, 450), "60 Bombs")
		tdif4.setSize(18)
		tdif4.setFill('pink')
		difficulty4.draw(win)
		tdif4.draw(win)

		#difficulty5
		difficulty5 = graphics.Rectangle(graphics.Point(300, 410),\
			graphics.Point(400, 490))
		difficulty5.setFill('black')
		tdif5 = graphics.Text(graphics.Point(350, 450), "300 Bombs")
		tdif5.setSize(18)
		tdif5.setFill('red')
		difficulty5.draw(win)
		tdif5.draw(win)

		#difficulty6
		difficulty6 = graphics.Rectangle(graphics.Point(450, 410),\
			graphics.Point(550, 490))
		difficulty6.setFill('black')
		tdif6 = graphics.Text(graphics.Point(500, 450), "700 Bombs")
		tdif6.setSize(18)
		tdif6.setFill('red')
		difficulty6.draw(win)
		tdif6.draw(win)

		#select difficulty text
		select_text = graphics.Text(graphics.Point(350, 200), "Select Your")
		select_text.setSize(30)
		select_text.draw(win)
		dif_text = graphics.Text(graphics.Point(350, 240), "Difficulty")
		dif_text.setSize(30)
		dif_text.setStyle('bold italic')
		dif_text.draw(win)

		difficulty = 0

		#keep asking for a level difficulty until user chooses
		while difficulty == 0:
			mouse = win.getMouse()
			if 310 < mouse.getY() < 390:
				if 150 < mouse.getX() < 250:
					difficulty = 17
				if 300 < mouse.getX() < 400:
					difficulty = 13.6
				if 450 < mouse.getX() < 550:
					difficulty = 6.8
			if 410 < mouse.getY() < 490:
				if 150 < mouse.getX() < 250:
					difficulty = 4
				if 300 < mouse.getX() < 400:
					difficulty = 2
				if 450 < mouse.getX() < 550:
					difficulty = 1

			if difficulty in (17,13.6,6.8,4,2,1):
				difficulty1.undraw()
				tdif1.undraw()
				difficulty2.undraw()
				tdif2.undraw()
				difficulty3.undraw()
				tdif3.undraw()
				difficulty4.undraw()
				tdif4.undraw()
				difficulty5.undraw()
				tdif5.undraw()
				difficulty6.undraw()
				tdif6.undraw()
				select_text.undraw()
				dif_text.undraw()
				return difficulty

class Game:
	'''
	The main Game class that constructs the game and plays it
	'''
	def __init__(self):
		'''constructs the initial game by calling functions
		'''
		#creates window
		self.win = graphics.GraphWin("Minesweeper 9000", 700, 700)

		#asks user for desired difficulty level
		self.difficult_level = cell.difficulty(self.win)

		#initialize the win lose conditions, the lists
		#of revealed and flagged cells, and set the exploded bomb cell to none
		self.won = False
		self.bomb = False
		self.revealed_cells = []
		self.flagged = {}
		self.exploded_bomb = None

		#sets the background
		background.set_background(self.win)

		#creates the cell list, bomb list, and cell number dictionary with the difficulty
		self.celllist = cell.cells(self.difficult_level)
		self.bomblist = cell.set_bombs(self.difficult_level)
		self.cell_nums = cell.get_nums(self.difficult_level, self.celllist, self.bomblist)

		#set grid and colors
		background.create_board(self.win, self.difficult_level, self.celllist)

	def reveal(self, cell_to_reveal):
		'''Reveals a cells number value or a bomb
		Parameters:
			cell_to_reveal: the cell to reveal bomb or number
		'''
		#if the cell is invalid, end function
		if cell_to_reveal == None:
			return
		
		#if the cell is a bomb, explode the cell and stop the function
		if self.cell_nums[cell_to_reveal] == '':
			animations.bombs(self.win, cell_to_reveal, self.difficult_level)
			self.bomb = True
			self.exploded_bomb = cell_to_reveal
			return

		#draws the number of surrounding bombs according to the self.cell_nums dictionary value
		text = graphics.Text(graphics.Point(cell_to_reveal[0],cell_to_reveal[1]), \
			self.cell_nums[cell_to_reveal])
		text.setFill('black')
		text.draw(self.win)

		#adds cell to revealed cell list
		self.revealed_cells.append(cell_to_reveal)

		#generates a list of neighbors depending on difficulty level
		a = self.difficult_level * 10
		neighbors = ((-a,a),(0,a),(a,a),(a,0),(a,-a),(0,-a),(-a,-a),(-a,0))

		if self.cell_nums[cell_to_reveal] == 0: #if the cell has zero bombs around it
			for neigh in neighbors: #iterate over the neighbors
				if ((cell_to_reveal[0] + neigh[0]) > 10) and \
				((cell_to_reveal[0] + neigh[0]) < 690) and \
				((cell_to_reveal[1] + neigh[1]) > 10) and \
				((cell_to_reveal[1] + neigh[1]) < 690): #if the neighbor is in bounds
					if ((cell_to_reveal[0] + neigh[0]), (cell_to_reveal[1] + neigh[1]))\
					 not in self.revealed_cells: #if the neighboring cell is not already revealed
						self.reveal((cell_to_reveal[0] + neigh[0], cell_to_reveal[1] + neigh[1]))
						#recursively call reveal on the neighbording cell

	def cell_clicked(self):
		'''Searchs for the cell that was clicked and how it was
		and returns a list containing the cell that was clicked
		or flags the cooresponding cell and returns
		Parameters:
			None
		'''
		click = self.win.getMouseWithButton()
		width = self.difficult_level * 5

		point = (int(click[0].getX()),int(click[0].getY()))

		if click[1] == 2 or click[1] == 3: #if user inputs a right click
			for cell in self.cell_nums: #iterate over the cells
				cell_to_flag = button.wasClicked(point, self.celllist, width) #get cell that was clicked
				if cell_to_flag != None: #if cell is a legal cell (not on the border)
					if cell_to_flag not in self.flagged: #if not already flagged
						if cell_to_flag not in self.revealed_cells: #if cell is not already revealed
							self.flagged[cell_to_flag] = \
								animations.flag(self.difficult_level, cell_to_flag)
							self.flagged[cell_to_flag].draw(self.win) #draw a flag at in the cell
							return('', 2) #end the function
					else: #if already drawn, undraw
						self.flagged[cell_to_flag].undraw()
						del self.flagged[cell_to_flag] #delete flagged cell from the dictionary
						return('', 2) #end the function
		else: #if user inputs a left click
			cell_to_reveal = button.wasClicked(point, self.celllist, width)
			if cell_to_reveal not in self.flagged: #if the clicked spot is not a flagged cell
				return (cell_to_reveal, 1) #return the cell and the type of click


		return(None, 2) #if runs function and if and else statements fail, won't crash program

	def close(self):
		'''Closes the window
		Parameters:
			None
		'''
		self.win.close()

	def winner(self):
		'''Called if the player wins the game and congratulates them
		with celebratory explosions
		Parameters:
			None
		'''
		#draws celebratory explosions around
		for size in range(0,30,4):
			animations.explosion(self.won, (370,200), size + 50, self.win)
			animations.explosion(self.won, (200,500), size + 20, self.win)
			animations.explosion(self.won, (580,450), size + 40, self.win)
			animations.explosion(self.won, (75,75), size, self.win)

		#congratulates the player
		congratsbackground = graphics.Rectangle(graphics.Point(250,310), \
			graphics.Point(450,355))
		congrats = graphics.Text(graphics.Point(350,332), 'Congrats!')
		congrats.setFill('black')
		congrats.setStyle('bold italic')
		congrats.setSize(36)
		congratsbackground.setFill('white')
		congratsbackground.draw(self.win)
		congrats.draw(self.win)

	def loser(self):
		'''Called if the user loses and draws explosions and
		encouraging phrases
		Parameters:
			None
		'''
		for size in range(0,20,4):
			animations.explosion(False, (200,500), size + 20, self.win)
			animations.explosion(False, (580,450), size + 40, self.win)
			animations.explosion(False, (75,75), size, self.win)

		failbackground = graphics.Rectangle(graphics.Point(250,310), \
			graphics.Point(450,355))
		fail = graphics.Text(graphics.Point(350,332), 'FAIL')
		fail.setFill('black')
		fail.setStyle('bold italic')
		fail.setSize(36)
		failbackground.setFill('white')
		failbackground.draw(self.win)
		fail.draw(self.win)

		#mean titles to sass the player for loosing
		mean = graphics.Text(graphics.Point(200,150), 'Do it again, but... uh... better...')
		mean.setFill('black')
		mean.setStyle('bold')
		mean.setSize(12)
		mean.draw(self.win)

		mean2 = graphics.Text(graphics.Point(500,550), "Hint: don't click the bombs")
		mean2.setFill('black')
		mean2.setStyle('bold')
		mean2.setSize(12)
		mean2.draw(self.win)

		mean3 = graphics.Text(graphics.Point(100,510), "Having fun yet?")
		mean3.setFill('black')
		mean3.setStyle('bold')
		mean3.setSize(12)
		mean3.draw(self.win)

	def play(self):
		'''Is the main game loop and will coordinate
		all the other functions and determine if the player
		has won
		Parameters:
			None
		'''
		while self.won != True and self.bomb != True: #while player hasn't hit a bomb or won
			cell = self.cell_clicked() #get the cell clicked
			if cell == None: #if the click returns an illegal click, don't crash
				'do nothing'
			elif cell[0] == None:#if the click returns an illegal click, don't crash
				'do nothing' 
			elif cell[1] == 1: #if the click was a left click
				if cell[0] not in self.revealed_cells: #if the cell is not already revealed
					self.reveal(cell[0]) #reveal the cell

			#the win condition: if the number of revealed equals 
			#the number of cells minus the number of bombs
			if len(self.celllist) - len(self.bomblist) == len(self.revealed_cells):
				self.won = True

		#After the while loop is broken:

		#if the player won
		if self.won == True:
			#if there aren't too many cells
			if self.difficult_level > 3:
				#undraw the flags
				for flag in self.flagged:
					self.flagged[flag].undraw()
				#draw the bombs
				for cell in self.bomblist:
					self.reveal(cell)
			
			#run the winner code
			self.winner()
		
		#if the player hit a bomb
		else:
			for size in range(0,30,4): #explode the cell they hit
				animations.explosion(False, self.exploded_bomb, size + 50, self.win, 'orange')
		
			#pause for a second
			time.sleep(.3)
			
			#if there aren't too many cells
			if self.difficult_level > 3:
				#undraw the flags
				for flag in self.flagged:
					self.flagged[flag].undraw()
				#reveal the bombs
				for i in self.bomblist:
					self.reveal(i)

			#run the losing code
			self.loser()

		#pause the code for .3 seconds and then continue
		time.sleep(.3)

		playAgain = 'idk'
		already_drawn = 'no'
		#ask if the player wants to play again and respond accordingly
		while playAgain == 'idk':
			playAgain = play_minesweeper_again.ask(self.win, already_drawn)
			already_drawn = 'yes'
		if playAgain == "Yes":
			self.close()
			game = Game()
			game.play()
		else:
			self.close

def main():
	'''Constructs a Minesweeper game by calling Game
	'''
	minesweeper = Game()
	minesweeper.play()

if __name__ == '__main__':
	main()