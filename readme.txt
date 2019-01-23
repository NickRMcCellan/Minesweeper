"""
Make sure to fill in the following information before submitting your
assignment. Your grade may be affected if you leave it blank!
For usernames, make sure to use your Whitman usernames (i.e. exleyas). 
File name: readme.txt
Author username(s): mcclelnr
Date: December 12th, 2017
"""

A description of your program and its features:

The file minesweeper9000.py is a simulation of the 1989 game Minesweeper. It runs in a 700 by 700 pixel window, and has six difficulty levels: 4, 6, 20, 60, 300, and 700 bombs to clear. For levels 4-20 there is the option of colorful cells, but when the cells get small enough it’s hard to read the text in the cells when they’re colorful. The program randomly generates bombs throughout the field, gets the number of bombs around each non-bomb cell, and will display this number when the user clicks on each non-bomb cell. The upper left cell is always a free space. If the clicked on cell is a 0 the program will automatically reveal all neighboring cells that are within the grid. If the user clicks a bomb it will explode and the losing sequence will run. If the user clears the board and places flags for every bomb, the winning sequence will run. At the end of either of these two outcomes it will prompt the user to either Quit or Play Again. It will then close the window and either quit the program or open a new game window.


A brief description and justification of how it is constructed (classes, functions, etc.):

Minesweeper9000 requires two files to run, a standard graphics.py file (that you've edited with the getMousewithbutton() function), and the minesweeper.py file itself.
There are a total of six classes in the program (button, background, play_minesweeper_again, animations, cell, and the main Game class). When main() is run, it creates a Game class. This class will:
1. Create a 700 x 700 pixel window
2. Prompt the user for desired difficulty level by calling the class cell and function difficulty
3. Sets the Game instance self variables and win/lose conditions to the default values
4. Sets the background by calling the background class and the set_background
5. Then sets the cell list, bomb list, and cell numbers by calling the cell class and the corresponding function
6. If the difficulty is under 20 bombs, it will ask the user for the desired color. In either case, it will draw the cells to the board
Each function is commented line by line (for lines that need explanation) for the working of each individual function.


A discussion of the current status of your program, what works and what doesn’t, etc.

Most things work, if there is anything that doesn’t it’s because it’s a unforeseen end case (if there are any problems, my guess would be with the Game.cell_clicked function). I tried to cover for cases when the cell_clicked function returned an invalid cell to the Game.play function (example, if the user clicked around the border of the game and not in a cell) with lines 589-592, but who knows. One area that could be improved is the game board generation, it takes it awhile to randomly generate 700 bombs, but I'm sure there is a better way of doing this that I have yet to learn. After all, it's my first ever project! I might’ve missed something. Otherwise everything is working how I intended it to. In a future update, I might want to update the explosion graphic to make it more interesting, but honestly I kind of like the simplicity of it because it’s an old 90s game after all!
