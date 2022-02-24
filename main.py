'''
File Name: main.py
Author: Adam Hoffmeister
Purpose: Create a visual simulation repreenting the Langton's ant 
on an infinite scale.  
'''
from graphics import graphics
from board import Board 

def main():
    print("Please press 1 if you would like to view the infinite snail program")
    print("in slow motion. Press 2 if you would like to view the program")
    print("at a fast pace.")
    
    user_input = int(input("Enter 1 (slow) or 2 (fast):"))
    
    if user_input == 1:
        frame_rate = 5 
    else:
        frame_rate = 60 
    
    wid = 700
    hei = 700
    win = graphics(wid, hei,"infinite snail")
    board = Board(win)
    while not win.is_destroyed():
        # decpict initial board layout 
        board.print_board()
        if board.get_orientation() == 0 or board.get_orientation() == 2:
            win.rectangle((335), (320), 40, 60, 'brown')
        else: 
            win.rectangle((315), (335), 60, 40, 'brown')
        win.update_frame(frame_rate)

        # show snail changing direction   
        board.snail_change_or()
        if board.get_orientation() == 0 or board.get_orientation() == 2:
            win.rectangle((320), (320), 40, 80, 'white')
        else: 
            win.rectangle((320), (340), 80, 40, 'white')
        board.print_board()
        win.update_frame(frame_rate) 

        # move snail 
        board.snail_move()
        
    

if __name__ == "__main__":
    main() 