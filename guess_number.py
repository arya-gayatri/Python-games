# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
# initialize global variables used in your code

num_range=100
max_choices=7
secret_number=0
i=0
# define event handlers for control panel
def init():
    frame.start()
    print "New Game. Range is from 0 to",num_range
    print "Number of remaining guesses is",max_choices
    print ""
    
    
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range=100
    global max_choices
    max_choices=7
    global secret_number
    secret_number = random.randrange(0,num_range)
    
    init()
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range=1000
    global max_choices
    max_choices=10
    global secret_number
    secret_number = random.randrange(0,num_range)
    init()
   
i=0 
def get_input(guess):
    # main game logic goes here	
    global i
    if i < max_choices and i > -1:
     number=int(guess)
     print "Guess was",number
     print "Number of remaining guesses is ", max_choices-(i+1)
     if max_choices-(i+1)==0 and number!=secret_number:
            print "You ran out of guesses. The number was",secret_number
            print ""
            init()
     else:
                if number == secret_number:
                 print 'Correct!'
                 print ''
                 init()
                elif number > secret_number:
                 print 'Lower!'
                else:
                 print "Higher!"
                
     i=i+1
     print ""
     
            
    else:
        print ''
     
   
     

     
    
    
# create frame
frame=simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements

frame.add_button("Range:0 - 100",range100,200)
frame.add_button("Range:0 - 1000",range1000,200)
frame.add_input("Enter your guess",get_input,200)

# start frame

init()

# always remember to check your completed program against the grading rubric
