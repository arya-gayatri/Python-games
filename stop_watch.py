# template for "Stopwatch: The Game"
import simplegui
# define global variables
t=0
x=0
y=0
countgames=0
countwins=0
milliseconds=0

# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global milliseconds
    minutes = t//600
    seconds = (t%600)//10
    milliseconds= t % 10
    if seconds<10:
        return str(minutes) + ":" + "0"+ str(seconds) + "." + str(milliseconds)
    else:
        return str(minutes) + ":" + str(seconds) + "." + str(milliseconds)
        
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    global x,y
    x=0
    y=0
    
def stop_handler():
    timer.stop()
    global x
    x=x+1
    if(x==1):
        global countgames
        countgames=countgames+1
        
    global milliseconds
    global countwins
    global y
    y=y+1
    if(milliseconds==0 and y==1):
        countwins=countwins+1
   
    
    
    
def reset_handler():
    timer.stop()
    global t
    global countgames
    global countwins
    t=0
    x=0
    y=0
    countgames=0
    countwins=0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t=t+1
    
def draw(canvas):
    canvas.draw_text(format(t),[150,100],40,"white")
    canvas.draw_text(str(countwins)+ "/"+ str(countgames),[320,40],30,"green")
    
    

    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 200)
timer=simplegui.create_timer(100,tick)


# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",start_handler,100)
frame.add_button("Stop",stop_handler,100)
frame.add_button("Reset",reset_handler,100)

# start timer and frame
frame.start()



# remember to review the grading rubric
  


