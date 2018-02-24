# "Guess the number" mini-project

# this project will use the SimpleGUI module that is unique to CodeSkulptor
# This module will allow us to set inputs into the console using a pop-up GUI
# All output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secret_num = 0
guesses_left = 0


# helper function to start and restart the game
def new_game():  
    global num_range
    global secret_num
    global guesses_left
    
    secret_num = random.randrange(0, num_range)
    
    if num_range == 100 : 	
        guesses_left = 7
    elif num_range == 1000 :
        guesses_left = 10
      
    print "New game. The range is between 0 and", num_range, ". Good luck!"
    print "You have ", guesses_left, "remaining! \n"
    pass

# define event handlers for control panel
def range100():
    # function for using number range from 0 to 100
    global num_range
    num_range = 100 
    new_game() 
    pass

def range1000():
    # function for using number range from 0 to 1000
    global num_range
    num_range = 1000
    new_game()
    pass
    
def input_guess(guess):    
    # main game logic
    global guesses_left
    global secret_num 
    
    won = False
    
    print "You guessed: ",guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left, "."
    
    if int(guess) == secret_num:       
        won = True
    elif int(guess) > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
    if won:
        print "That is correct! Congratulations!\n"
        new_game()
        return
    elif guesses_left == 0:
        print "Game over. You ran out of guesses."   
        new_game()
        return
    else:
        print result
        pass
    
# create frame
f = simplegui.create_frame("Game: Guess the number!", 250, 250)
f.set_canvas_background('Green')

# register event handlers for control elements
f.add_button("Set range between 0 and 100.", range100, 100)
f.add_button("Set range between 0 and 1000.", range1000, 100)	
f.add_input("Enter your guess", input_guess, 100)

# call new_game and start frame
new_game()
f.start()