'''
'''

from random import randint 
from enum import Enum 

class Node:
    def __init__(self, val): 
        '''
        val is deltaOrientation 
        '''
        self.val = val 
        self.next = None
        self.generate_color() 

    def generate_color(self):
        x = randint(0,8)
        color = color_cor(x)
        self.color = color

class ColorCircle:
    def __init__(self):
        head = Node(randint(0,3))
        
        for i in range(8):
            if i == 0:
                temp = Node(randint(0,3))
                first = temp 
            else:
                new = Node(randint(0,3))
                temp.next = new 
                temp = new 
        temp.next = head 
        head.next = first 
        self.head = head 

def color_cor(x):
    assert 0 <= x <= 8  
    c1 = ["pink", "blue", "green", "purple", "orange", "red"]
    c2 = ["yellow", "cyan", "magenta"]
    colors = c1 + c2 
    return colors[x]

