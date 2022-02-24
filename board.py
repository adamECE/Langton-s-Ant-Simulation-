'''
board.py 
- standard board size will be 10 
'''
from cell import Cell 
from snail import Snail
from generate import ColorCircle 
# from three_shapes_game import Game 
import graphics

class Board: 
    def __init__(self, win):
        '''
        The board class is intended to represent a board 
        of size 7x7. Within the board,  
        '''
        c = ColorCircle()
        # self._size = 10 
        self._cells = {(0,0): Cell(c.head)} 
        self._cur_position = (0,0)
        self._snail = Snail()
        self._win = win 
        
    def snail_move(self):    
        self._snail.move(self._cells[(self._snail.x,self._snail.y)])
        x = self._snail.x
        y = self._snail.y
        if (x,y) not in self._cells:
            c = ColorCircle()
            self._cells[(self._snail.x,self._snail.y)] = Cell(c.head)
        
    def snail_change_or(self):
        x = self._snail.x
        y = self._snail.y
        self._snail.change_oreintation(self._cells[(x,y)])

    def get_orientation(self):
        return self._snail.get_dir() 

    def print_board(self):
        board_positions = {}
        pos = self._snail.get_position()
        x = pos[0]
        y = pos[1]

        for i in range(7,-1,-1):
            for j in range(8):
                board_positions[(i-1,j-1)] = (((x-4 + i),(y-4+j)))

        for pos, actual_pos in board_positions.items():
            if actual_pos not in self._cells:
                x = pos[0] 
                y = pos[1]
                self._win.rectangle((x*100), (y*100), 100, 100, 'black')
            else:
                x = pos[0] 
                y = pos[1]
                xa = actual_pos[0]
                ya = actual_pos[1]
                self._win.rectangle((x*100), (y*100), 100, 100, self._cells[xa,ya].get_color())

       
        





    





