'''
cell.py 
'''
from generate import ColorCircle

class Cell: 
    def __init__(self, color):
        '''
        colors is the head node of a LL  
        '''
        self._color = color
    

    def change_color(self):
        self._color = self._color.next 
    
    def get_deltaO(self):
        return self._color.val 
    
    def get_color(self):
        return self._color.color



