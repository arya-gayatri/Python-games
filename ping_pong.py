# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[7,-3]
paddle1_pos=[100,280]
paddle2_pos=[100,280]
paddle1_vel=2 
paddle2_vel=2
score1=0
score2=0

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel,PAD_WIDTH,WIDTH,BALL_RADIUS # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if right==True:
        ball_vel[0]=(random.randrange(120,240))/40
    elif right==False:
        ball_vel[0]=-(random.randrange(120,240))/40
        
    
    ball_vel[1]=-(random.randrange(60,180))/40
    return ball_pos, ball_vel
    
    
    

# define event handlers
def init():
    global ball_pos,paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2 
    sound=simplegui.load_sound("http://www.flashkit.com/imagesvr_ce/flashkit/soundfx/Interfaces/Switches/SwitchOn-SCOOB200-7374/SwitchOn-SCOOB200-7374_hifi.mp3")
    sound.play()
    ball_pos=[WIDTH/2,HEIGHT/2]
    ball_vel=[7,-3]
    paddle1_pos=[160,240]
    paddle2_pos=[160,240]
    score1=0
    score2=0
    paddle1_vel=0
    paddle2_vel=0
    
    # these are ints
   

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,PAD_WIDTH,right,PAD_HEIGHT,paddle1_vel,paddle2_vel,HEIGHT
 
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos[0]+=paddle1_vel
    paddle2_pos[0]+=paddle2_vel
    paddle1_pos[1]+=paddle1_vel
    paddle2_pos[1]+=paddle2_vel
    
    
    if paddle2_pos[0]>HEIGHT-PAD_HEIGHT or paddle2_pos[0]<0:
        paddle2_pos[0]+=-paddle2_vel
        paddle2_pos[1]+=-paddle2_vel
        
    if paddle1_pos[0]>HEIGHT-PAD_HEIGHT or paddle1_pos[0]<0:
        paddle1_pos[0]+=-paddle1_vel
        paddle1_pos[1]+=-paddle1_vel
        
    if paddle1_pos[1]>HEIGHT or paddle1_pos[1]<PAD_HEIGHT:
        paddle1_pos[1]+=-paddle1_vel
        paddle1_pos[0]+=-paddle1_vel
        
    if paddle2_pos[1]>HEIGHT or paddle2_pos[1]<PAD_HEIGHT:
        paddle2_pos[1]+=-paddle2_vel
        paddle2_pos[0]+=-paddle2_vel
        
        
    # draw mid line and gutters
  
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
   
    
    
    
    
    
    
    # draw paddles
    
    c.draw_polygon([(0, paddle1_pos[0]),(PAD_WIDTH, paddle1_pos[0]),(PAD_WIDTH,paddle1_pos[1]),(0,paddle1_pos[1])], 3, "red","red")
    c.draw_polygon([(WIDTH, paddle2_pos[0]),(WIDTH, paddle2_pos[1]),(WIDTH-PAD_WIDTH,paddle2_pos[1]),(WIDTH-PAD_WIDTH,paddle2_pos[0])], 3, "yellow","yellow")
    
    
    
     
    # update ball
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    if ball_pos[1]<=BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
        sound = simplegui.load_sound("http://renpygen.thelibrarygame.net/renpygen/images/6/6d/Pong_boop.wav")
        sound.play()
    if ball_pos[1]>=(HEIGHT-1)-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
        sound = simplegui.load_sound("http://renpygen.thelibrarygame.net/renpygen/images/6/6d/Pong_boop.wav")
        sound.play()
        
    
    
        
        
    if (ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS)):
        if (ball_pos[0]<=(PAD_WIDTH+BALL_RADIUS) and ball_pos[1]>paddle1_pos[0] and ball_pos[1]<paddle1_pos[1]):
            sound=simplegui.load_sound("http://renpygen.thelibrarygame.net/renpygen/images/c/cc/Pong_beep.wav")
            sound.play()
            ball_vel[0] = -1.10*ball_vel[0]
            ball_vel[1]=ball_vel[1]
           
        else:
            sound=simplegui.load_sound("http://www.flashkit.com/imagesvr_ce/flashkit/soundfx/Interfaces/Switches/SwitchOn-SCOOB200-7374/SwitchOn-SCOOB200-7374_hifi.mp3")
            sound.play()
            right=True
            score2=score2+1
            ball_init(right)
       
    if (ball_pos[0]>=(WIDTH-PAD_WIDTH-BALL_RADIUS)):    
        if (ball_pos[0]>=(WIDTH-PAD_WIDTH-BALL_RADIUS) and ball_pos[1]>paddle2_pos[0] and ball_pos[1]<paddle2_pos[1]):
            sound=simplegui.load_sound("http://renpygen.thelibrarygame.net/renpygen/images/c/cc/Pong_beep.wav")
            sound.play()
            ball_vel[0] = -1.10*ball_vel[0]
            ball_vel[1]=ball_vel[1]
          
            
        else:
            sound=simplegui.load_sound("http://www.flashkit.com/imagesvr_ce/flashkit/soundfx/Interfaces/Switches/SwitchOn-SCOOB200-7374/SwitchOn-SCOOB200-7374_hifi.mp3")
            sound.play()
            right=False
            score1=score1+1
            ball_init(right)
    
    
    
    
            
    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,2,"navy","white")
    c.draw_text(str(score1), (240, 50), 50, "red")
    c.draw_text(str(score2), (330, 50), 50, "yellow")
   
        
def keydown(key):
    acc=10
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=acc
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=acc
   
def keyup(key):
   
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("green")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", init, 100)


# start frame
init()
frame.start()

