# implementation of card game - Memory

import simplegui
import random

memorydeck=[i%8 for i in range(16)]



# helper function to initialize globals
def init():
    global state
    state=0
    global i,j,moves
    moves=0
    l.set_text("Moves =0")
    global exposed
    random.shuffle(memorydeck)
    exposed=[False for i in range(16)]
    

     
# define event handlers
def mouseclick(pos):
    global state,i,j,moves,exposed
    x=0
    x=pos[0]//50
   
    if state==0 or state==1 or state==2:
        if state==0:
            exposed[x]=True
            i=x
            state=1
        elif state==1:
            exposed[x]=True
            j=x
            state=2
        elif state==2:
            if memorydeck[i]!=memorydeck[j]:
                if exposed[i]==True:
                    exposed[i]=False
                   
                if exposed[j]==True:
                    exposed[j]=False
                    
            exposed[x]=True    
            i=x
            moves+=1
            l.set_text("Moves ="+str(moves))
            state=1
          
            
       
        
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global moves,exposed
    for i in range(0,16):
        if exposed[i]==True:
            canvas.draw_text(str(memorydeck[i]),[i*50,75],50,"fuchsia")
        else:
            if i==0:
                canvas.draw_polygon(([0,0],[50,0],[50,100],[0,100]),4,"aqua","blue")
            else:
                canvas.draw_polygon(([i*50,0],[i*100,0],[i*100,100],[i*50,100]),5,"aqua","blue")
            
            
       
          
      
            
            
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves =0")



# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_canvas_background("navy")
frame.set_draw_handler(draw)

# get things rolling
frame.start()
# Always remember to review the grading rubric