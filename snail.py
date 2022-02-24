'''
snail.py
0,1,2,3 = NESW  
'''
from enum import Enum 
from cell import Cell 



class Snail:
    def __init__(self):
        self._dir = 0
        self.x = 0 
        self.y = 0 
    
    def move(self, cell):
        if self._dir == 0:
            self.y += 1
        elif self._dir == 1: 
            self.x += 1 
        elif self._dir == 2:
            self.y -= 1 
        else:
            self.x -= 1 
        
        cell.change_color() 

    def change_oreintation(self, cell):
        deltaOr = cell.get_deltaO()

        if deltaOr < 0: 
            deltaOr = - deltaOr
            for i in range(deltaOr): 
                self._dir -= 1 
                if self._dir == -1: 
                    self._dir = 3
        else: 
            for i in range(deltaOr):
                self._dir += 1 
                if self._dir == 4:
                    self._dir = 0 

    def get_position(self):
        '''
        returns position in a form of a tuple 
        '''
        return((self.x,self.y))

    def get_dir(self):
        return self._dir 