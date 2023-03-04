# Portfolio Project 3 - Battleships, Python
![battleships](https://user-images.githubusercontent.com/122393963/222894089-99d8d54d-eca3-4a2d-8bb0-f94f030faace.png)

[Project website](https://pproject-3-battleships.herokuapp.com/)

## How to play
- Player enter a number between 1 and 5 for row and column.
- "X" indicates a hit on the board while a message saying "It's a hit!" when guessing right on a ship.
- If you guess wrong and miss it says "You missed!"
- If you guess the same combination of row's and column's a message saying "You've already guessed that!" will show.
- If you manage to hit all ships, it says "You sunk my ship!" and the game ends (you will have to click run program again to restart).

## Features
### Existing Features
- Random generation of ship-placement.
- The ships are hidden.
- Board layout 5x5.
- Can only put in numbers and cannot leave the input field empty, if so an error occurs and you will have to click "run program" yet again to restart.

![battleships 2](https://user-images.githubusercontent.com/122393963/222896203-9a7eea3e-8762-40a9-8aa3-ad4aa8f6ee57.png)

![battleships 3](https://user-images.githubusercontent.com/122393963/222896309-c85c014e-fa10-4f1d-a58c-ce70435d3983.png)

### Future Features
- Fix so you can only put in numbers between 0 and 4.
- Not be able to enter same guess twice.
- Fix so you can't enter coordinates outside of the board grid.
- Make it possible to see player board, computer board and play against each other.

## Data Model
I used list comphrehension and dims to make a square 5x5 board.

## Testing
- Tested in PEP8, which gave all but two codes a pass (52: E702 multiple statements on one line (semicolon), 67: E702 multiple statements on one line (semicolon)).
- Tested so right message comes up to right input/value.
- Tested in local terminal and the Code Institute Heroku terminal.

### Bugs
- When you put in the first row/column numbers at the start of the game, the terminal shows everything but a message if you hit, miss, etc.
- After the first input, if you for example type "row 1, col 2" and then put it in again right after, it will show up same message as the time before and not say that
you already guessed that.
- Sometimes it will say "You sunk my ship!" without showing actual hits on the board.

## Deployment
- Using Code Institute's Python Terminal on Heroku.


## Credits
- Code Institute for the Python Essentials Template and Terminal.
- I took help from [this](https://bigmonty12.github.io/battleship) tutorial to get help with knowing how to code and build structure. Didn't have enough time to sit
and think and figure things out enough for it to click. I if I had more time I would have changed a lot more and make it a bit more advanced than what it is, my idea
was to make it so you had a board for both a player and the computer, as I mentioned in "Future Features".
- Took some inspiration from the video "Portfolio Project Scope" for "Portfolio 3: Project Submisson" by Code Institute when it comes to some of the layout.
