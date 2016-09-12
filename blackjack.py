# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
msg1='Hit or stand?'
msg2=''
n=0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
            
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]	

    def __str__(self):
        return str([str(card) for card in self.hand])	
        
    def hit(self,card):
        sound = simplegui.load_sound("http://www.soundjay.com/misc/sounds/page-flip-1.mp3")
        sound.play()
        self.hand.append(card)
     
    def get_value(self):
        hand_value=0
        for item in self.hand:
            hand_value=hand_value+VALUES[item.get_rank()]
        
        if 'A' in item.get_rank():
            
            if (hand_value+10)>21:
                hand_value=hand_value+0
            else:
                hand_value=hand_value+10
               
                
        else:
            
            hand_value=hand_value+0
            
        return hand_value
                
            
      
    
    def draw(self, canvas,pos):
        global n
        xpos=100
        for item in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(item.get_rank()), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(item.get_suit()))
            
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [xpos + CARD_CENTER[0], pos], CARD_SIZE)
            xpos=xpos+100
            
            
            if n==0:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [135.5, 250], CARD_BACK_SIZE)
            
            
            
            
# define deck class
class Deck:
    def __init__(self):
        self.deck=[]
        for s in SUITS:
            for r in RANKS:
                self.deck.append(Card(s,r))
        

    
    def shuffle(self):
        random.shuffle(self.deck)
        sound = simplegui.load_sound("http://www.soundjay.com/misc/shuffling-cards-1.mp3")
        sound.play()

def deal():
    global outcome,in_play,msg1,n,msg2
    d.shuffle()
    player.hand=[]
    dealer.hand=[]

    i=0
    n=0
    for i in range(2,4):
        player.hit(d.deck[i])
        dealer.hit(d.deck[i+2])
        i=i+1
    in_play = True
    n=0
    msg1="Hit or stand?"
    msg2=''

def hit():
     
    global score,msg1,msg2
    if player.get_value()<=21:
        d.shuffle()
        i=random.randint(0,50)
        player.hit(d.deck[i])
        if player.get_value()>21:
            msg2="You have busted"
            msg1="New Deal?"
            sound = simplegui.load_sound("http://www.allmusiclibrary.com/free_sound_effects/disenchant.mp3")
            sound.play()
            score=score-1
    
   

       
def stand():
        
    global score,n,msg1,msg2,in_play
    n=1
    if player.get_value()>21:
        
        msg2="You went bust and lose"
        n=1
        msg1="New Deal?"
        sound = simplegui.load_sound("http://www.allmusiclibrary.com/free_sound_effects/disenchant.mp3")
        sound.play()
        score=score-1
        in_play=False
    else:
        while dealer.get_value()<17:
            i=random.randrange(0,52)
            d.shuffle()
            dealer.hit(d.deck[i])
        if dealer.get_value()>21:
        
            msg2="You win"
            msg1="New Deal?"
            sound = simplegui.load_sound("http://www.allmusiclibrary.com/free_sound_effects/enchant.mp3")
            sound.play()
            score=score+1
            in_play=False
        else:
            if player.get_value()<=dealer.get_value():
            
                msg2="You lose"
                msg1="New Deal?"
                sound = simplegui.load_sound("http://www.allmusiclibrary.com/free_sound_effects/disenchant.mp3")
                sound.play()
                score=score-1
                in_play=False
            else:
               
                msg2="You win"
                msg1="New Deal?"
                sound = simplegui.load_sound("http://www.allmusiclibrary.com/free_sound_effects/enchant.mp3")
                sound.play()
                score=score+1
                in_play=False

# draw handler    
def draw(canvas):
    global msg
    canvas.draw_text("BLACKJACK",[100,70],50,"lime")
    canvas.draw_text("Score="+str(score),[465,60],30,"white")
    canvas.draw_text("Dealer",[100,150],30,"yellow")
    dealer.draw(canvas,250)
    player.draw(canvas,500)
    canvas.draw_text("Player",[100,400],30,"yellow")
    canvas.draw_text(msg1,[300,400],30,"white")
    canvas.draw_text(msg2,[300,150],30,"white")
    
   
     

# initialization frame
frame = simplegui.create_frame("Blackjack", 800, 600)
frame.set_canvas_background("teal")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
player=Hand()
dealer=Hand()
d=Deck()


# deal an initial hand
i=0
for i in range(2):
    d.shuffle()
    player.hit(d.deck[i])
    dealer.hit(d.deck[i+2])
    i=i+1




# get things rolling
frame.start()


# remember to review the gradic rubric