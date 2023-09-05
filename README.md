# UcTasMinimax
An AI for the traditional Turkish Game called "Üç Taş" or "Three Men Morris" based on depth-limited minimax algorithm  and written in python
# Rules:
- Each player has three pieces.
- The winner is the first player to align their three pieces on a row or a column on the board. 
- There are 3 horizontal lines, 3 vertical lines and 2 diagonal lines.
- The board is empty to begin the game, and players take turns placing their pieces on empty intersections. Once all pieces are placed (assuming there is no winner by then), play proceeds with each player moving one of their pieces per turn. A piece may move to any vacant point on the board, not just an adjacent one.

# Setup
- Download the repository  
- Open terminal and change the terminal directory as the root direcotry of the project.
- Run `pip install pygame` in the terminal if  pygame is not already installed.
- Run  `python runner.py` in the terminal.
- Enjoy the game!

# Playing 

- Use left click to move or select a piece.
- If you selected a piece unintetionally use right click to deselect it.


# Some Notes
- The game is designed to be Turkish so the texts in the game are written in Turkish.
- For now player can only play in white pieces but I may add a better version with better UI and the ability to switch colors.
- You can change the depth of ai via changing the variable called `DEPTH` currently it is 8.
