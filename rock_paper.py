# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random
import math

def number_to_name(number):
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    if number==0:
        name='rock'
    elif number==1:
          name='Spock'
    elif number==2:
          name='paper'
    elif number==3:
          name='lizard'
    else:
          name='scissors'
                        
    return name
    
def name_to_number(name):
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    if name=='rock':
        number=0
    elif name=='Spock':
        number=1
    elif name=='paper':
        number=2
    elif name=='lizard':
        number=3
    else:
        number=4
        
    return number


def rpsls(guess):
    #  converts guess into the number player_number between 0 and 4
    
    return name_to_number(guess)
    
    
    
def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number=name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,4)
    # compute difference of player_number and comp_number modulo five
    difference=(player_number - comp_number) % 5
    # use if/elif/else to determine winner
    if difference==1 or difference==2:
        winner='Player'
    elif difference==3 or difference==4:
        winner='Computer'
    else:
        winner='No one'
    # convert comp_number to name using number_to_name
    comp_choice=number_to_name(comp_number)
    
    # print results
    print "Player chooses", name
    print "Computer chooses", comp_choice
    print winner, "wins!"
    print ''
    
# test your code
'''
a=number_to_name(0)
print a
b=name_to_number('paper')
print b
'''
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

